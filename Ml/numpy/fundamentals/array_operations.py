import numpy as np
a=np.arange(1,11)
b=np.arange(1,11)
print(a)

#scalar operations
#arithmetic
print(a*2)
#like this we can do all+-*/**,etc

#relational
print(a>5)
#can use all ><,==,>=,<=,!=



#vector operations
#arithmetic
print(a*b)
# acn use all but remember of row and col part
#also can do relational in the same case


#array func
a1=np.random.random((3,3))
a1=a1*100
print(a1)
print(np.prod(a1))
print(np.max(a1)) #awa sum and min
print(np.max(a1,axis=0))#col->0 and row ->1
#can also use like this mean/median/std/var


#dot product
a=np.arange(1,13).reshape(3,4)
b=np.arange(1,13).reshape(4,3)
#its like (p,q) and (q,r) hence should worry about q val
print(np.dot(a,b))
print(np.exp(a))
print(np.log(a))

#round/floor/ceil
c=np.round(np.random.random((2,3))*100)
print(c)
#round do roundoff
#ceil shift aage wale int pe
#floor will do piche wale int pe