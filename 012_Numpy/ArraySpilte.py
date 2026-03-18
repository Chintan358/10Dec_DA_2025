import numpy as np

# a = np.array([10,20,30,40,50,60])
# k = np.array_split(a,3)
# print(k[1])


a = np.array([[10,20,30,78,70],[40,50,60,9,75]])
k = np.array_split(a,2,axis=1)
print(k)