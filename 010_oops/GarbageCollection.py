import sys

x = [1,2,3]
y=x
z = x
y = None
print(sys.getrefcount(x))