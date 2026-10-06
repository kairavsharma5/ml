import pandas as pd
import numpy as np
a=pd.read_csv('subs.csv').squeeze("columns")
#print(type(a))
#print((a))
b=pd.read_csv('kohli_ipl.csv',index_col=("match_no")).squeeze("columns")
#b = pd.read_csv('kohli_ipl.csv', index_col='match_no')['runs']    this line is also valid the video is a bit old thats why this can be added as changes
# because of this we can see match no. also
#print(b)
#print(type(b))
c=pd.read_csv('bollywood.csv',index_col=("movie")).squeeze("columns")
#print(c)
# always the name in o/p will be the opposite one from the indexcol whichever goes in for val


# METHODS

#head and tail method
d=a.head(9)  # give top n      , by default it give top 5
#print(d)
e=a.tail(9) #give last n        ,by default it give last 5

#sample movie
f=c.sample()   # gives a random val from dataset   , in paranthese can give int and it will give that many val
#print(f)

#value_count
g=c.value_counts()
#print(g)


#sort_values
h=b.sort_values(ascending=False).head(1).values[0]   
# in paranthese always do this if needed becaus default asscending is true
#.values will give val but in numpy arr so to get only normal val we do the index part
#print(h)


#sort_index
i=c.sort_index(ascending=False)
#print(i)



#MATH METHODS

#count
k=b.count()
#print(k)
#sum
j=b.sum()
#print(j)
#product
l=b.product()
#print(l)

#mean,median,mode,var,std
m=c.mode()
#print(m)

#SAME CAN DO WITH MIN/MAX

#DESCRIBE
n=b.describe() # give summary of all maths quant
print(n)
 