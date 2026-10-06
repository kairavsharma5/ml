import pandas as pd
import numpy as np
a=pd.read_csv('subs.csv').squeeze("columns")
b=pd.read_csv('kohli_ipl.csv',index_col=("match_no")).squeeze("columns")
c=pd.read_csv('bollywood.csv',index_col=("movie")).squeeze("columns")
print(b[-8:])
#fancy indexing
print(b[[1,23,5,8,1]])