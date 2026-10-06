import pandas as pd
import numpy as np

# series from list
'''country=["ind","pak","nep","sri"]
a=pd.Series(country)
print(a)
bat=[1,2,3,321,23,1,3]
b=pd.Series(bat)
c=b.astype(np.int32)
print(b)
print(c)'''
# custom index
'''marks=[123,1,31,3]
sub=["eng","maths","sst","sci"]
a=pd.Series(marks,index=sub)
print(a)   # in this index is changed by name of sub 


#setting a name
b=pd.Series(marks,index=sub,name="number hai")
print(b)'''


# marks from dict
marks={
    "eng":213,
    "math":123,
    "sci":1212

}
a=pd.Series(marks)
print(a)