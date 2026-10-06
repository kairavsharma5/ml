import pandas as pd
import numpy as np

marks={
    "eng":213,
    "math":123,
    "sci":1212

}
a=pd.Series(marks)
s=a.size
k=a.dtype
q=a.is_unique
p=a.index
m=a.values
print(s)
print(k)
print(q)
print(p)
print(m)
print(type(m))