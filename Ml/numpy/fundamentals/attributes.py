import numpy as np
a=np.arange(1,11)
b=np.arange(1,11).reshape(5,2)
c=np.arange(1,9).reshape(2,2,2)
d=b.ndim# tells the dimension of array
#shape
e=b.shape  #gives the shape
print(e)

f=b.size    #tells the size of array
print(b)
g=b.itemsize   #how much size does array takes
print(g)
print(b.dtype)

