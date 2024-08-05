import pandas as pd
df = pd.read_csv('GoogleApps.csv')
#print(df["Content Rating"].value_counts())

temp=df["Content Rating"].value_counts()
#print(temp["Everyone"])
#print(temp["Everyone 10+"])
#print(temp["Everyone"]/temp["Everyone 10+"])

#print(df.groupby(by='Content Rating')['Size'].mean())
#print(df.groupby(by='Content Rating')['Size'].agg(['min','max','mean']))

#print(df["Category"].value_counts()["BUSINESS"])

#print(temp["Teen"]/temp["Everyone 10+"])

print(round(df.groupby(by='Type')['Rating'].mean(),2))
