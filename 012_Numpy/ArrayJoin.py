import numpy as np

# a = np.array([
#                [1,2,4],
#                [3,4,4],
#                [3,4,4]  ])
# b = np.array([ 
#                 [5,6,9],
#                 [7,8,7],  
#                 [7,8,7]]  )

# # k = np.concatenate((a,b))
# k = np.concatenate((a,b),axis=1)
# print(k)

# a = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
# b = np.array([[[10,20],[30,40]],[[50,60],[70,80]]])

# k = np.concatenate((a,b),axis=2)
# print(k)


a = np.array([10,20,30])
b = np.array([30,40,60])

# k = np.concatenate((a,b),axis=1)
k = np.stack((a,b),axis=0)
print(k.ndim)
print(k)
