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

import re

a = "movie is not fdfd poor "
k = re.sub(r"not\s+\w+\s+poor", "good", a)
print(k)
