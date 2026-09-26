import numpy as np
a=np.arange(1,11)
b=np.arange(1,13).reshape(3,4)
c=np.arange(1,13).reshape(3,4)
# we can do stacking   #shape should always be same
#horizonatl stacking
d=np.hstack((b,c))
print(d,"\n")
e=np.vstack((b,c))
print(e,"\n")

f=np.hsplit(d,2)
print(f)
g=np.vsplit(e,3)
print(g)
