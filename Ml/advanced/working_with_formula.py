import numpy as np

#sigmoid fuc
'''def sigmoid(arr):
    return 1/(1+np.exp(-arr))
a=np.arange(10)
b=sigmoid(a)
print(b)'''


#mean sq error
actual=np.random.randint(1,50,25)
predicted=np.random.randint(1,50,25)
def mse (actual,predicted):
    a=np.mean(actual-predicted)**2
    return a

b=mse(actual,predicted)
print(b)
