import pandas as pd
import matplotlib.pyplot as pyplot
s=pd.Series(data=[10,5,15,20,10],index=[1,2,3,4,5])
s.plot()
plt.show()
#df = pd.read_csv('GoogleApps.csv')
#print(df["Content Rating"].value_counts())
#print(pd.isnull(df["Category"]).head())
#df['Rating'].fillna(-1,inplace=True)
#temp=df["Content Rating"].value_counts()
#print(temp["Everyone"])
#print(temp["Everyone 10+"])
#print(temp["Everyone"]/temp["Everyone 10+"])

#print(df.groupby(by='Content Rating')['Size'].mean())
#print(df.groupby(by='Content Rating')['Size'].agg(['min','max','mean']))

#print(df["Category"].value_counts()["BUSINESS"])

#print(temp["Teen"]/temp["Everyone 10+"])

#print(round(df.groupby(by='Type')['Rating'].mean(),2))
