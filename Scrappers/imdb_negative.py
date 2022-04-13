# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 22:23:12 2019

@author: Prateek
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 10:26:20 2019

@author: Prateek
"""


import requests
import bs4
import pandas as pd 
#main > div > div.lister.list.detail.sub-list > div > div:nth-child(1) > div.lister-item-content > h3 > a
def homepage(path):
    top_250_ratings = []
    selector = r"#main > div > div.lister.list.detail.sub-list > div > div:nth-child("
    title_selector = r") > div.lister-item-content > h3 > a"
    rating_selector = r") > div.lister-item-content > div > div.inline-block.ratings-imdb-rating > strong"
    res = requests.get(path)
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    j=1
    for i in range(1, 251): 
        css_container_title = soup.select(selector+str(j)+title_selector)
        css_container_rating = soup.select(selector+str(j)+rating_selector)
        css_container_link = r"https://www.imdb.com" + css_container_title[0].get('href')
        print(i)
        top_250_ratings.append([css_container_title[0].text, css_container_rating[0].text, css_container_link])
        if i%50 == 0:
            next_path = r"https://www.imdb.com/search/title/?groups=bottom_250&sort=user_rating,asc&start=" + str(i+1)
            res = requests.get(next_path)
            soup = bs4.BeautifulSoup(res.text, 'html.parser')
            j=1
        else:
            j+=1
            
        
        
    return top_250_ratings
        

final = homepage("https://www.imdb.com/search/title/?groups=bottom_250&lists=!watchlist&sort=user_rating,asc")
print(final)

data2 = pd.DataFrame(final, columns=["title", "rating", "link"])

data2.to_csv("movie_data_negative_another.csv")