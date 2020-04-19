import pandas as pd
import csv


#with open('predata.csv') as f:
data = pd.read_csv('nptelhrd.csv', encoding = 'unicode_escape')
 #data = f.read() 
duration = data['duration']
# outfile = open("predata.csv", "a")
# write_outfile = csv.writer(outfile)
d =[]
i = 0
for t in duration:
  if len(t) == 7:
      if t[3] == 'M':
          d.append( 60 * int(t[2]) + int(t[4])*10 + int(t[5]))
          i+=1
      elif t[6] == 'M':
          d.append(60*60 * int(t[2]) + 600 * int(t[4]) + 60 * int(t[5]))
          i+=1
      elif t[6] == 'S' and t[3]=='H':
          d.append(60*60 * int(t[2]) + 10 * int(t[4]) + 1 * int(t[5]))
          i+=1
      else:
           d.append(600*int(t[2]) + 60*int(t[3]) + int(t[5]))
           i+=1
  elif len(t) == 6:
        if t[3] == 'M':
            d.append(60*int(t[2]) + int(t[4]))
            i+=1
        elif t[5] == 'M':
            d.append(60*60* int(t[2]) + 60 * int(t[4]))
            i+=1
        else :
            d.append(3600 * int(t[2]) + int(t[4]) )
  elif len(t) == 5:
      if t[4] == 'M':
        d.append(600*int(t[2]) + 60*int(t[3]))
        i+=1
      else:
           d.append(10*int(t[2]) + int(t[3]))
           i+=1
  if len(t) == 8:
         if t[3] =='H':
             d.append( 3600* int(t[2]) + 600* int(t[4]) +  int(t[6]))
             i+=1
         else:
             d.append(600*int(t[2]) + 60*int(t[3]) + int(t[5])*10 + int(t[6]))
             i+=1
         
  
  elif len(t) == 4:
      if t[3] == 'M':
         d.append(60*int(t[2]))
         i+=1
      else:
         d.append(int(t[2]))
         i+=1
  elif len(t) == 9:
      if t[5] == 'M':
          d.append( 3600* int(t[2]) + 60* int(t[4]) + 10* int(t[6]) + int(t[7]))
          i+=1
      else:
          d.append(3600* int(t[2]) + 600* int(t[4]) + 60*int(t[5]) + int(t[7]))
          i+=1
  elif len(t) == 10:
      d.append(3600* int(t[2]) + 600* int(t[4]) + 60*int(t[5]) + 10* int(t[7]) + int(t[8]) )
      i+=1

      
 
# write_outfile.writerows(map(lambda x: [x],d))       

     

#add coloum to csv 
data["time"] = d
data.to_csv("nptelhrd.csv", index=False)
      

           
         
            
    
    