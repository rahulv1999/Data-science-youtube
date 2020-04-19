#main part
import csv
api_key="AIzaSyC27cunFzrq-ti5nHUiwYHCG0ZGzlg2XZw"
from apiclient.discovery import build
youtube =build('youtube','v3',developerKey=api_key)
type(youtube)
print(youtube)

def get_channel_videos(id1):
    
    # get Uploads playlist id
    res = youtube.channels().list(id=id1, part='contentDetails').execute()

    playlist_id = res['items'][0]['contentDetails']['relatedPlaylists']['uploads']
    
    #['items'][0]
    videos = []
    next_page_token = None
    
    while 1:
        res = youtube.playlistItems().list(playlistId=playlist_id,part='snippet,contentDetails',maxResults=50,pageToken=next_page_token).execute()
        videos += res['items']
        next_page_token = res.get('nextPageToken')
        
        if next_page_token is None:
            break
    
    return videos

    # res1 = youtube.videos().list(id=id1, part='sta').execute()

def deEmojify(inputString):
    return inputString.encode('ascii', 'ignore').decode('ascii')


id1=input("enter the channelupload playlist id")
videos = get_channel_videos(id1)
with open('channel_videos.csv', 'w',encoding='utf-8',newline='') as csvFile:
                fields=['VideoName','VideoId','PublishDate']
                writer = csv.writer(csvFile)
                writer.writerow(fields)
                for video in videos:


                    output=deEmojify(video['snippet']['title'])
                    data=[[output,video['contentDetails']['videoId'],video['contentDetails']['videoPublishedAt']]]
                    writer.writerows(data)
