import numpy as np


# a = np.array([10,20,30])
# a = np.array([[1,2,3],[4,5,6]])
# a = np.array([
#     [[1,2],
#      [3,4]],

#     [[1,2],
#      [3,4]],

#     [[1,2],
#      [3,4]]])


# print(a)
# print(a.shape)
# print(a.dtype)
# print(a.size)
# print(a.ndim)



# a = np.zeros((2,3,5),int)
# a[0][0][0] = 20
# print(a)

# a = np.ones((2,3,5),int)
# a[0][0][0] = 20
# print(a)

# a = np.arange(1,10)
# print(a)

# a = [10,20,30,40]
# b = [60,70,80,90]
# print(a+b)

# a = np.arange(1,10)
# b= np.arange(11,20)

# print(a)
# print(b)

# print(a+b)
# print(np.add(a,b))


# a = np.linspace(1,10,5)
# print(a)

# a = np.eye(5,5,k=3)
# print(a)


# a = np.array([[1,2,3],[4,5,6],[7,8,9]])
# b = np.array([[1,2,3],[4,5,6],[7,8,9]])

# print(a*b)


# k = np.empty((2,2))
# print(k)


# arr = np.random.rand(2, 3)
# print(arr)

# arr = np.random.randn(2, 2)
# print(arr)

# arr = np.random.randint(1, 100, (2, 3))
# print(arr)

# arr = np.random.choice([10, 20,100,500, 30, 40], size=3)
# print(arr)



# np.random.seed(1)
# arr = np.random.rand(3)
# print(arr)


arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [4, 5, 6]])

# print(arr.itemsize)
# print(arr.nbytes)

# k = arr.ravel()

# k = arr.flatten()
# k[0] = 400
# print(k)
# print(arr)

# k = np.array([10,20,30,40,50,60])
# p = k.reshape((2,3))
# print(p)

# print(arr.T)

# k = np.array([10,20,30,40,50,60,70])
# r = np.where(k>30,"A","B")
# print(r)


# a = np.array([[1, 2], [3, 4]])
# b = np.array([[5, 6], [7, 8]])

# result = np.stack((a, b))
# print(result)

# a = np.array([[1, 2], [3, 4]])
# b = np.array([[5, 6], [7, 8]])

# result = np.dstack((a, b))
# print(result)


arr = np.array([1,5, 2, 2, 3, 4, 4])

# print(np.unique(arr))
# print(np.sort(arr))
# print(np.argsort(arr))
# print(np.where(arr > 3))

# arr = np.array([True])

# print(np.all(arr))

# print(np.clip(arr, 1, 4))

# arr = np.array([5, 10, 15,16,21, 20])

# print(np.clip(arr, 8, 18))

# arr = np.array([1, np.nan, 3])
# print(np.nanstd(arr))

k = np.array([[10,20,30,40,50,60],
              [100,200,300,400,500,600]])
# print(k[::-1])
# print(k[0,3])

# print(k[::1, :])