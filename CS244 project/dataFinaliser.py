import csv
import pandas as pd

with open("finishedData1_nptel.csv",'w', encoding = 'latin-1') as df:
    writer = csv.writer(df)
    fields = ['channelTitle','videoId','channelId','title','viewCount','likeCount','dislikeCount','commentCount','time','commentScore']
    writer.writerow(fields)
    print("1")
    f = pd.read_csv("nptelhrd.csv")
    c = pd.read_csv("commentScore_nptel.csv")
    channelTitle = f['channelTitle']
    videoId  = f['videoId']
    cvideoId = c['videoId']
    channelId = f['channelId']
    title = f['title']
    viewCount = f['viewCount']
    likeCount = f['likeCount']
    dislikeCount = f['dislikeCount']
    commentCount = f['commentCount']
    time = f['time']
    commentScore= c['score']
    print(time[3])
    for i in range(len(c)):
        for j in range(len(f)):
            # print(cvideoId[i])
            # print(videoId[j])
            if(cvideoId[i] == videoId[j] ):
                data = [channelTitle[j], videoId[j], channelId[j] , title[j], viewCount[j], likeCount[j],  dislikeCount[j], commentCount[j], time[j], commentScore[i]]
                print("1")
                print(data)
                writer.writerow(data)
                print("2")
            
                
    