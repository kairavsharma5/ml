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

#ipl final winner
finale_counter=b['MatchNumber']=='Final'
#print(b[finale_counter][['Season', 'WinningTeam']])


#how many matches supeer over haas occured
super_over=b['SuperOver']=='Y'
#print(b[super_over].shape[0])   #shape tells teh rows and columns of df

#how many matches has csk win in kolkata
city=b[(b['City']=='Kolkata')&(b['WinningTeam']=='Chennai Super Kings')]
#print(city.shape[0])

#action movuies imdb>7
movies=a[(a['genres'].str.contains('Action')) & (a['imdb_rating']>7.5)]
print(movies)
#if you have to do by the below one then remove .contain par then add .split  then .apply
#.apply (lambda x:'Action in x )works like at every iteration it goes to each x and ask if action is in there
#.str change it in str ,then split do the division