# f = open("D://test.txt",'w')
# # f.write("Hello, someting")
# f.writelines(["Hello python\n","Hello Tops\n","Hello World"])
# f.close()


# f = open("test.txt",'a')
# f.write("Hello, something")
# f.close()


# f = open("D://test.txt",'r')
# data = f.read()
# print(data)
# f.close()


# f = open("test.txt",'r')
# data = f.readlines()
# print(data)
# f.close()



# f = open("test.txt",'r')
# while True:
#     data  = f.readline()
#     # if "Hello" in data:
#     #     print(data)
#     if not data:
#         break
#     print(len(data))
# f.close()


# with open("test.txt") as f :
#     f.seek(10)
#     print(f.tell())
#     data = f.read()
#     print(f.tell())
#     print(data)

# with open("home.txt",'w+') as f:
#     f.write("something")
#     f.seek(0)
#     data = f.read()
#     print(data)


# with open("home.txt",'r+') as f:
#     # f.seek(0)
#     f.write("XYZ")
#     data = f.read()
#     print(data)


# with open("logo.png",'rb') as f:
#     data = f.read()
#     print(data)