import numpy as np
import pandas as pd
list
student_data=[
    [100,123,123],
    [213,31,31],
    [13,345,74]
]
a=pd.DataFrame(student_data,columns=['iq','age','lpa'])
#using 
#print(a)


#using dict
student_dict={
    'iq':[23,123,1,12],
    'age':[231,123,11,23],
    'goal':[12,123,13,23]

}
b=pd.DataFrame(student_dict)
#print(b)  #because of this you dont have to specify columns because they are already pre defined


#using_read.csv
c=pd.read_csv('movies.csv')
#print(c)
d=pd.read_csv('ipl-matches.csv')
print(d)