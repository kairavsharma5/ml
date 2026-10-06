import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
a=pd.read_csv('subs.csv').squeeze("columns")
b=pd.read_csv('kohli_ipl.csv',index_col=("match_no")).squeeze("columns")
c=pd.read_csv('bollywood.csv',index_col=("movie")).squeeze("columns")
#print(len(a))
#print(type(a))
#print(dir(a)) #returns a list of the names (attributes and methods)
#print(sorted(a)) #sorts the val
#min max 


#type conversion
d=list(a)
#print(d)
#print(type(d))
#membership operators can also be done ( this will search things only on index for values you have to write .values at last)
#LOOPING CAN ALSO BE DONE AWA ARITHMETIC AND RELATIONAL OPERATORS


#BOOLEAN INDEXING ON SERIES
#print(b>50) 
#print(b[b>50].size) #this will make it as a overlapping series

# GRAPH

e=a.plot()
#plt.show()
f=c.value_counts().head(20).plot(kind="pie")
plt.show()
#print(f)
