import numpy as np

# a = np.array([10,20])
# b = np.array([10,40])
# k = np.logical_xor(False,True)
# print(k)

# k = np.not_equal(a,b)
# print(k)


# a = np.array([[10,20],[40,50]])
# b = np.array([[10,20],[1,5]])

# k = a+b
# print(k)


a = np.array([[10,20],[22,56]])
b = np.array([[10,40,45],[40,50,45]])

a_p = np.pad(a,((2,1),(1,1)),mode='constant')

a_p[0][0] = 80
print(a_p)
# k = np.concatenate((a_p,b))
# print(k)


# A = np.array([[1, 2], [3, 4], [5, 6]]) # 3x2
# B = np.array([[7, 8], [9, 0]])         # 2x2


# B_padded = np.pad(B, ((1, 1), (1, 1)), 'constant') 

# print(B_padded)

# result = np.hstack((A, B_padded))
# print(result)
