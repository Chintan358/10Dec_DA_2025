# # *****
# # *****
# # *****
# # *****
# # *****

# lines = 5
# for i in range(lines):
#     for k in range(lines-i):
#         print(" ",end="")
#     for j in range(i+1):
#         print("*",end="")
#     print()
# lines = 4
# for i in range(lines):
#     for k in range(i+2):
#         print(" ",end="")
#     for j in range(lines-i):
#         print("*",end="")
#     print()

# import re

# a = "movie is not fdfd poor "
# k = re.sub(r"not\s+\w+\s+poor", "good", a)
# print(k)


list_of_tuples = {"python":10,"java":10}

# Unpack the list of tuples into separate iterators
unzipped_iterators = zip(*list_of_tuples)

# print(dict(unzipped_iterators))



# k = ["1","2","3"]
# j = ["A","B","C"]
# i = ["X","Y","Z"]
# d = zip(k,j,i)

# print(list(d))

# k = zip(*d)
# print(list(next(k)))
# print(list(next(k)))
# print(list(next(k)))


d = {"1":"sagar","3":"krushang","2":"hasan","70":"Amit"}
# k = sorted(d.values())
# u = {}

# for l in k :
#     for k,v in d.items():
#         if v==l:
#            u.update({k:v})

# print(u)

k = sorted(d.items(),key=lambda i : i[0])
print(dict(k))
