# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 16:57:07 2019

@author: Prateek
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 14:11:25 2019

@author: Prateek
"""

import pandas as pd

data1 = pd.read_csv(r"E:\Coding\python\Web\review_data.csv", index_col=0)
data2 = pd.read_csv(r"E:\Coding\python\Web\review_data_negative_another.csv", index_col=0)

data = data1.append(data2)

import nltk

from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(min_df=2, tokenizer=nltk.word_tokenize)
life = cv.fit_transform(data["review"])

from sklearn.feature_extraction.text import TfidfTransformer
tfidfvec = TfidfTransformer()
X = tfidfvec.fit_transform(life)
y = data["metascore"].values//51
print("Vectorizing completed")

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, shuffle=True)
#
#del X;
#del y;

from sklearn.naive_bayes import MultinomialNB
classifier = MultinomialNB()
classifier.fit(X,y)
print("model trained")

#del X_train;
#del y_train;

y_pred = classifier.predict_proba(X_test)
y_pred2 = classifier.predict(X_test)

from sklearn.metrics import accuracy_score
cm = accuracy_score(y_test, y_pred2)
print(cm)




def selfpredict(sent):
    ctrans = cv.transform(sent)
    tf_trans = tfidfvec.transform(ctrans)
    if classifier.predict(tf_trans)[0] == 2:
        print("Positive Review")
    elif classifier.predict(tf_trans)[0] == 0:
        print("Negative Review")
    else:
        print("Neutral Review")



selfpredict(["It was the worst movie"])
f = open('my classifier', 'wb')
import pickle
pickle.dump(classifier, f)
f.close()

