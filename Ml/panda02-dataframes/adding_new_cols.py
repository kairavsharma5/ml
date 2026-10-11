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
#adding completely new cols
a['Country']='India'
#print(a)

#by existing col
a.dropna(inplace=True)  #this removes the whole row where a single val is missed ,weve done this because in the df there were some rows in which actor's name was not given
a['lead-actor']= a['actors'].str.split('|').apply(lambda x: x[0])
print(a.head())