api_key = "AIzaSyCxJdAlVeRen_CC-oqNBg_2SEgvkaz2fR0"
from apiclient.discovery import build
youtube = build('youtube', 'v3', developerKey=api_key)

def get_channel_videos(channel_id):
    
    # get Uploads playlist id
    res = youtube.channels().list(id=channel_id, 
                                  part='contentDetails').execute()
    playlist_id = res['items'][0]['contentDetails']['relatedPlaylists']['uploads']
    
    videos = []
    next_page_token = None
    
    while 1:
        res = youtube.playlistItems().list(playlistId=playlist_id, 
                                           part='snippet', 
                                           maxResults=50,
                                           pageToken=next_page_token).execute()
        videos += res['items']
        next_page_token = res.get('nextPageToken')
        
        if next_page_token is None:
            break 
    
    return videos

videos = get_channel_videos('UCkUq-s6z57uJFUFBvZIVTyg')

#for video in videos:
#    print(video['snippet']['title'])
print(videos[0])