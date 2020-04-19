import pandas as pd
import csv
from random import seed
from random import randint

df = pd.read_csv("finishedData1.csv")
data = df.drop(['title','channelId', 'videoId' ,'channelTitle' ], axis=1)
data1 = data['viewCount']
data2 = data['likeCount']
data3 = data['dislikeCount']
data4 = data['commentCount']
data5 = data['time']
data6 = data['commentScore']

print(data)
label = [[.65,.2,-0.3,.1,0.05,0.2],[0.5,0.27,-0.31,0.15,0.02,0.3],[0.49,.32,-.32,.4,0,0.11],[0.5,0.32,-0.45,0.20,0.05,.4]]
y=[] 
for i in range(len(data)):
      j = randint(0,3)
      print(j)
      y.append(label[j][0]*data1[i] + label[j][1]*data2[i]+ label[j][2]*data3[i]+ label[j][3]*data4[i]+ label[j][4]*data5[i]+ label[j][5]*data6[i]),
    
     
      

df['Y'] = y
df.to_csv("finishedData1.csv", index = False)
print(y)