import pandas as pd
df = pd.read_csv(r"C:\Users\DELL\Downloads\data.csv")

#print(df.info())
#print(df.isnull().sum())

#df = df.fillna(0)
#ages = df[df['age']>25]
#print(ages)

#df['total'] = df['a'] + df['b']
print(df.head())

#res = df.groupby('category')['sales'].sum()
#print(res)

#rescount = df.groupby('category')['sales'].count()
#print(rescount)

#resavg = df.groupby('category')['sales'].mean()
#print(resavg)

