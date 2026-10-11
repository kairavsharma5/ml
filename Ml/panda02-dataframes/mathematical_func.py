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
student_dict={
    'name':['gost','cheeta','sher','wdas'],
    'iq':[23,123,1,12],
    'age':[231,123,11,23],
    'goal':[12,123,13,23]

}
d=pd.DataFrame(student_dict)

#print(c.sum())  # it will automatically by col. if you have to do by row do axis=1 in ()
# same for min ,mean,max,mode,median,std 


#selecting col from dataframe
#SINGLE COL
#print(a['title_x'])
#print(b['Venue'])

#MULTI COLUMNS
#print(b[['ID','City','Date']])




d.set_index('name',inplace=True)  #this will change the auto generated index to the name col as index
"""print(d)       inplace change in real df

##fethching rows in df
single row
print(a.iloc[5])"""

#multiple rows
#print(a.iloc[0:5:2])

#print(d.loc['gost':'sher'])


#SELECTING BITH ROW AND COL
print(a.iloc[0:3,0:3])