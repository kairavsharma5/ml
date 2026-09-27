import numpy as np
a= np.arange(24).reshape(6,4)
#print(a,"\n")
#fancy indexing
'''print(a[[0,2,3]],"\n")
print(a[[0,2,3,5]],"\n")
print(a[:,[0,2,3]],"\n")'''


#boolean indexing

b=np.random.randint(1,100,24).reshape(6,4)
#print(b,"\n")
#print(b>50,"\n")
#print(b[b>50])  # by writing this way ive chnaged the array itself which means ive put the condn directly to no. by excluding t/f
#print(b,"\n")
print(b[b%2==0],"\n")