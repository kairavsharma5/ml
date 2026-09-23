import numpy as np
a=np.arange(1,11)
b=np.arange(1,11).reshape(5,2)
#astype   its used to change the no.of data type

c= a.astype(np.int32)
print(c.dtype)