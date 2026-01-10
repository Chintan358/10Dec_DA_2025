# number =17
# flag = 0
# for i in range(2,number):
#     rem = number%i
#     if rem==0:
#         flag=1
#         break
        
# if flag==0:
#     print("prime")
# else:
#     print("Not prime")


# for k in range(3,101):
#     number = k
#     flag = 0
#     for i in range(2,number):
#         rem = number%i
#         if rem==0:
#             flag=1
#             break
            
#     if flag==0:
#         print(f"{number} is prime")
#     else:
#         pass
#         # print(f" {number} is Not prime")





sum =0
for k in range(3,101):
    number = k
    flag = 0
    for i in range(2,number):
        rem = number%i
        if rem==0:
            flag=1
            break
            
    if flag==0:
        sum+=number
        print(f"{number} is prime")
    else:
        pass
        # print(f" {number} is Not prime")
print(sum)