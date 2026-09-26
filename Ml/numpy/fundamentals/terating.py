import numpy as np
a=np.arange(1,11)
b=np.arange(8).reshape(2,4)
c=np.arange(27).reshape(3,3,3)
#for i in a:
 #   print(i)
#for i in b:
#    print(i)
#for i in c:
#    print(i)
#for i in np.nditer(c): #this covertd 3d in 1d and then print 
 #   print(i)



#reshaping and one form of transpose
print(b)
d=np.transpose(b)
e=b.T   #these both means same
print(d)
print(e)
#it transpose the size of matrix/array

f=c.ravel()#change every array in 1d array
print(f)