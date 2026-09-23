import numpy as np
'''
a=np.array([1,2,3])
print(a)
print(type(a))
# for 2d ,3d array
b=np.array([[1,2,3],[2,1,3]])
print(b)
c=np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(c)
d=np.array([1,2,3],dtype="float")
print(d)
'''

#another way to create array
'''
a=np.arange(1,10)
print(a)
b=np.arange(1,10,2)
print(b)

#reshape

c=np.arange(1,11).reshape(5,2)  #(row,col)
print(c)
'''
a=np.ones((3,4)) #print only ones
print(a,"\n")
b=np.zeros((1,2))       #print only zeros
print(b)
c=np.random.random((2,2))       #print only random no.
print(c)
d=np.linspace(-10,10,10)  # (lower end,upperend,no.wanted)
print(d)
e=np.identity(3)  #makes identity matrix
print(e)