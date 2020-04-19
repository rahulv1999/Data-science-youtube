import pandas as pd
import numpy as np
from sklearn import preprocessing
import matplotlib.pyplot as plt 
plt.rc("font", size=14)
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import cross_val_predict
from sklearn.model_selection import train_test_split
from sklearn.svm import SVR

df = pd.read_csv("finishedData1.csv")
X = df.drop(['channelTitle','videoId','channelId','title','Y'], axis =1)
y = df['Y']
X_train, X_test,y_train,y_test = train_test_split(X,y,test_size = 0.3, random_state =0)
#Linear regression
clf1 = LinearRegression()
clf1.fit(X_train,y_train)
print(" Linear Regression score : " + str(clf1.score(X_test,y_test)))


#DecisionTree
clf2 = DecisionTreeRegressor()
clf2.fit(X_train,y_train)
# scores = cross_val_score(clf, X_test, y_test)
print(" DecisionTree score : " + str(clf2.score(X_train,y_train)))

#Support vector machines
clf3 = SVR(C=1, epsilon = 0.2)
clf3.fit(X_train,y_train)
print(" SVM score : " + str(clf3.score(X_train,y_train)))

#predict outcome

def mostInfluencialVideo(clf, f):
    data = f.drop(['channelTitle','videoId','channelId','title'], axis =1)
    v = clf.predict(data)
    v1 = max(v)
    for i in range(len(data)):
        if v[i] == v1:
            print("The most influencial video is :")
            print(f.loc[i,:])
df = pd.read_csv("finishedData1_nptel.csv",encoding = 'latin-1')  
print("******************Linear Regression******************")
mostInfluencialVideo(clf1,df)
print("******************DecisionTree******************")
mostInfluencialVideo(clf2,df)
print("******************SVM******************")
mostInfluencialVideo(clf3,df)



