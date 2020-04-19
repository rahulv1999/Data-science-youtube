import csv 
import pandas as pd

df = pd.read_csv("statnptel.csv", encoding = 'latin-1')
score = df['commentScore']
vid = df['videoId']
avg = 0
k=0
a =1
avg_data =[]
v = []
print(score, vid)
print(range(len(score)))
# for i in range(len(score)-1):
#       print("1")
#       for q in range(5):
#         avg += score[i]
#         k+=1
#         print("2")
#         print(avg,k,vid[i])
#         if( vid[i] is not vid[i+1]):
#           print(avg/k)
#           v.append((vid))
#           avg_data.append(avg/k,vid)
#           avg = 0
#           k=0
#           a=0
#           break
      

# print(avg_data)
# print(len(avg_data))
# print(v)
# print(len(v))

k=1
for i in range(len(score)-1):
    avg += score[i]
    if(vid[i] is vid[i+1]):
        k +=1
        pass
    else:
        avg_data.append(avg/k)
        v.append(vid[i])
        avg = 0
        k = 1

print(avg_data)
print(len(avg_data))
print(v)
print(len(v))
with open('commentScore_nptel.csv','w', encoding='utf-8') as df:
    writer = csv.writer(df)
    fields = ['videoId','score']
    writer.writerow(fields)
    for i in range(len(avg_data)):
        data = [v[i],avg_data[i]]
        writer.writerow(data)
    

    