import numpy as np
a=np.array([1,2,3,4,np.nan,6])
b=a[~np.isnan(a)]
print(b)   # by this we found the missing val , nan means missing values