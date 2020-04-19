#main part
import emoji
import csv
import pandas as pd
api_key="AIzaSyCxJdAlVeRen_CC-oqNBg_2SEgvkaz2fR0"
from apiclient.discovery import build
youtube =build('youtube','v3',developerKey=api_key)
type(youtube)
print(youtube)

def get_subs_ytb(channel_id):
    try:    
        res=youtube.channels().list(part="statistics",id=channel_id).execute()
        print(res['items'][0]["statistics"])
    except Exception:
            pass



        
def getting_desc_video(video_id):
    try:   
        req= youtube.videos().list(part='snippet,contentDetails',id=video_id).execute()
        #print(req['items'][1]['channelId'])
        print(req['items'][0]['snippet']['publishedAt'])
        print(req['items'][0]['snippet']['title'])
        str=req['items'][0]['contentDetails']['duration']
        print(str[2:])
    except Exception:
            pass

        


def get_video_comment(video_id):

    try:   
        comments =[]
        next_page_token= None

        while 1:
                res=youtube.commentThreads().list(part='snippet',videoId=video_id,maxResults=5,pageToken=next_page_token,textFormat="plainText").execute()
       #forcheckingwhat we want to display print(res['items'])
                comments +=res['items']
                next_page_token = None
        
                if next_page_token is None:
                        break
        return comments        
    except Exception:
            pass



def deEmojify(inputString):
    try:
       return inputString.encode('ascii', 'ignore').decode('ascii')
    except Exception:
        pass

        



df = pd.read_csv("nptelhrd.csv")
c = df[:]['channelId']
v = df[:]['videoId']
for i in range(len(c)):
    
    channel_id= c[i]
    video_id=v[i]
    get_subs_ytb(channel_id)
    getting_desc_video(video_id)
    comments=get_video_comment(video_id)
 

    with open('statnptel.csv', 'a',encoding='utf-8',newline='') as csvFile:
               try:
                fields=['Name','Comments','CommentId','viewerRating','LikeCount','PublishedAt','hours','videoId']
                writer = csv.writer(csvFile)
                writer.writerow(fields)
                for comment in comments:

                      publishedAt=comment['snippet']['topLevelComment']['snippet']['publishedAt']
                      inputString=comment['snippet']['topLevelComment']['snippet']['textDisplay']
                      comm=deEmojify(inputString)
                      data=[ [comment['snippet']['topLevelComment']['snippet']['authorDisplayName']
                            ,comm
                            ,comment['snippet']['topLevelComment']['id']
                            ,comment['snippet']['topLevelComment']['snippet']['viewerRating']
                            ,comment['snippet']['topLevelComment']['snippet']['likeCount']
                            ,publishedAt
                            ,publishedAt[11:13],str(video_id)]]
                     
                      writer.writerows(data)
               except Exception:
                            pass
       
                
