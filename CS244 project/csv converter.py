import json
import pandas as pd
import csv
field = ['channelId','videoId','channelTitle','title','viewCount', 'likeCount' ,'dislikeCount' ,
         'favoriteCount', 'commentCount' ,'duration']
with open("nptelhrd.json") as f:
    data = json.load(f)
outfile = open("nptel.csv", "w")
write_outfile = csv.writer(outfile)
write_outfile.writerow(field)
    #print(type(data))
   #data_str = json.dump(data, open('dt.json' , "w"))
   # print(data['UCX6b17PVsYBQ0ip5gyeme-Q']['video_data']['rlx6ur_D51s']['title'])
   # for vdata in data["video_data"][0]:
k = 'UC640y4UvDAlya_WOj5U4pfA'
    
for video_id in data[k]['video_data']:
      a = [k,video_id,
          data[k]['video_data'][video_id]['channelTitle'],
           data[k]['video_data'][video_id]['title'],
           data[k]['video_data'][video_id]['viewCount'],
           data[k]['video_data'][video_id]['likeCount'],
           data[k]['video_data'][video_id]['dislikeCount'],
           data[k]['video_data'][video_id]['favoriteCount'],
           data[k]['video_data'][video_id]['commentCount'],
           data[k]['video_data'][video_id]['duration']]
      write_outfile.writerow(a)
         
        