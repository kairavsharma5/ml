import numpy as np
a=np.arange(1,11)
b=np.arange(1,13).reshape(3,4)
c=np.arange(1,9).reshape(2,2,2)
#indexing 
print(a[-1])
print(a[1])
print(b[1,0]) #the val starts from 0 not from 1
print(c[1,1,1])
# for 3d first see in which 2d array it exist then go for 2d row,col

#slicing
print(a[2:5])  #same as py
print(b)
print(b[0,:1])
print(b[0,:])
 #empty for what row or col you ant full
print(b[1,:1:3])
# everyhing form 1 st row to 1,2 element of all the rest rows including 1
print(b[::2,::3])
print(b[::2,1::2])
print(b[0:2,1::2])