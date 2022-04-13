# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 10:26:20 2019

@author: Prateek
"""


import requests
import bs4
import pandas as pd 


def homepage(path):
    top_250_ratings = []
    selector = r"#main > div > span > div > div > div.lister > table > tbody > tr:nth-child("
    title_selector = r") > td.titleColumn > a"
    rating_selector = r") > td.ratingColumn.imdbRating > strong"
    res = requests.get(path)
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    for i in range(1, 101):
        css_container_title = soup.select(selector+str(i)+title_selector)
        css_container_rating = soup.select(selector+str(i)+rating_selector)
        css_container_link = r"https://www.imdb.com" + css_container_title[0].get('href')
        print(i)
        top_250_ratings.append([css_container_title[0].text, css_container_rating[0].text, css_container_link])
        
        
    return top_250_ratings
        

final = homepage("https://www.imdb.com/chart/bottom")
print(final)

data2 = pd.DataFrame(final, columns=["title", "rating", "link"])

data2.to_csv("movie_data_negative.csv")