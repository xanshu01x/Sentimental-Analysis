# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 15:42:35 2019

@author: Prateek
"""

import requests
import bs4
import pandas as pd

data = pd.read_csv(r"movie_data_negative.csv", index_col=0)
total_reviews = []
final_reviews = []
selector = r"#main > div:nth-child(1) > table > tbody > tr:nth-child("
score_selector = r") > td.score > div > span"
publisher_selector2 = r") > td.review > a > b > span"
publisher_selector = r") > td.review > b > span"
review_selector = r") > td.review > div"

for i in range(100):
    reviews = []
    path = data["link"][i]+r"criticreviews?ref_=ttexrv_ql_6"
    res = requests.get(path)
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    
    title = data["title"][i]
    rating = data["rating"][i]
    
    for j in range(10):
        css_container_score = soup.select(selector+str(j+1)+score_selector)
        css_container_publisher = soup.select(selector+str(j+1)+publisher_selector)
        if len(css_container_publisher) == 0:
            css_container_publisher = soup.select(selector+str(j+1)+publisher_selector2)    
        css_container_review = soup.select(selector+str(j+1)+review_selector)
        if len(css_container_score) == 0 and len(css_container_publisher) == 0 and len(css_container_review) == 0:
            break
        print('i =', i, ', j =', j)
        reviews.append([title, rating, css_container_score[0].text, css_container_publisher[0].text, css_container_review[0].text])
        
    if len(reviews) != 0:
        total_reviews.append(reviews)
        final_reviews += reviews
        
        
data2 = pd.DataFrame(final_reviews, columns=["title", "rating", "metascore", "publisher", "review"])

data2.to_csv("review_data_negative.csv")