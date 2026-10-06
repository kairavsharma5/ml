import pandas as pd
import numpy as np
a=pd.read_csv('subs.csv').squeeze("columns")
b=pd.read_csv('kohli_ipl.csv',index_col=("match_no")).squeeze("columns")
c=pd.read_csv('bollywood.csv',index_col=("movie")).squeeze("columns")
#using indexing
b[1]=100
print(b[1])
#can edit the same through slicing also by just giving the val through slicing
b[4:6]=[100,69]
print(b[3:7]) 
#can do fancy indexing in this also