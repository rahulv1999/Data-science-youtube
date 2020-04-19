# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 14:34:11 2020

@author: RV
"""
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyser = SentimentIntensityAnalyzer()
def print_sentiment_scores(sentence):
    snt = analyser.polarity_scores(sentence)
    # print("{:-<40} {}".format(sentence, str(snt)))
    return(snt)
d=[]
score=[]
v=[]
df = pd.read_csv("statnptel.csv", encoding='latin-1')
comment = df['Comments']
# vid = df['videoId']
for i in range(len(comment)):
    d = print_sentiment_scores(str(comment[i]))
    score.append(d['compound'])
    # v.append(vid[i])
    
print(score)
    
df['commentScore'] = score
# df['videoId']= vid
df.to_csv("statnptel.csv", index = False)