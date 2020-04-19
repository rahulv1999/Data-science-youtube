#main part
import emoji
import csv
import pandas as pd
from tqdm import tqdm
api_key="AIzaSyCxJdAlVeRen_CC-oqNBg_2SEgvkaz2fR0"
from apiclient.discovery import build
youtube =build('youtube','v3',developerKey=api_key)
type(youtube)
print(youtube)

def get_subs_ytb(channel_id):
        res=youtube.channels().list(part="statistics",id=channel_id).execute()
        print(res['items'][0]["statistics"])



        
def getting_desc_video(video_id):
        req= youtube.videos().list(part='snippet,contentDetails',id=video_id).execute()
        #print(req['items'][1]['channelId'])
        print(req['items'][0]['snippet']['publishedAt'])
        print(req['items'][0]['snippet']['title'])
        str=req['items'][0]['contentDetails']['duration']
        print(str[2:])

        


def get_video_comment(video_id):

        comments =[]
        next_page_token= None

        while 1:
                res=youtube.commentThreads().list(part='snippet',videoId=video_id,maxResults=100,pageToken=next_page_token,textFormat="plainText").execute()
       #forcheckingwhat we want to display print(res['items'])
                comments +=res['items']
                next_page_token = res.get('nextPageToken')
        
                if next_page_token is None:
                        break
        return comments        




def deEmojify(inputString):
    return inputString.encode('ascii', 'ignore').decode('ascii')

        



df = pd.read_csv("nptelhrd.csv")
details = df[:][:1]
d=[]
for i in details:
 channel_id=input(details['channelId'])
 video_id=input(details['videoId'])
 get_subs_ytb(channel_id)
 getting_desc_video(video_id)
 comments=get_video_comment(video_id)

 with open('stats.csv', 'w',encoding='utf-8',newline='') as csvFile:
                
                for comment in comments:

                     publishedAt=comment['snippet']['topLevelComment']['snippet']['publishedAt']
                     inputString=comment['snippet']['topLevelComment']['snippet']['textDisplay']
                     comm=deEmojify(inputString)
                     data=[[comment['snippet']['topLevelComment']['snippet']['authorDisplayName']
                            ,comm
                            ,comment['snippet']['topLevelComment']['id']
                            ,comment['snippet']['topLevelComment']['snippet']['viewerRating']
                            ,comment['snippet']['topLevelComment']['snippet']['likeCount']
                            ,publishedAt
                            ,publishedAt[11:13]]]
                     d.append(data)
                     pbar = tqdm(total=1)
                            
       
fields=['Name','Comments','CommentId','viewerRating','LikeCount','PublishedAt','hours']
                                
df[fields] = d
df.to_csv("nptelcom.csv", index = False)