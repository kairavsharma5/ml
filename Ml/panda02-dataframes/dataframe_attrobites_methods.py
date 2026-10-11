import numpy as np
import pandas as pd

a=pd.read_csv('movies.csv')
b=pd.read_csv('ipl-matches.csv')
student_data=[
    [100,123,123],
    [213,31,31],
    [13,345,74]
]
c=pd.DataFrame(student_data,columns=['iq','age','lpa'])

#print(a.shape)  

#print(a.dtypes)

#print(a.index)

#print(a.columns)
#print(b.values)
#print(b.head(3))
#print(a.tail(2))
#print(a.sample(2))  #tells the random data
#print(a.info())    #gives high level info of your data
#print(a.describe())          #gives numeric summary
#print(a.isnull().sum())    #this tell which which column does have missing values
#print(a.duplicated())  #tell how many duplicate rows are there can do .sum there to get a no. in return
c.rename(columns={'age':'umar','lpa':'package'},inplace=True)
#print(c)  #helps in renaming colums  if inplace is false it will change temporarily


#astype
print(b.info())
b['ID']=b['ID'].astype('Int32')
print(b.info())
