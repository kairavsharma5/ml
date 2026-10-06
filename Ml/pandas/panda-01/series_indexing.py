import pandas as pd
import numpy as np
a=pd.read_csv('bollywood.csv',index_col=("movie")).squeeze("columns")
x=pd.Series([1,23,3,1,312,4,46,446,75,56,844,67,4])
#print(x[2])
print(a['Fraud Saiyaan'])