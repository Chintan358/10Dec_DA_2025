# number = 153
# temp = number
# sum =0
# while number !=0:
#     rem = number%10
#     sum +=(rem**3)
#     number = number//10


# if temp == sum:
#     print("armstrong")
# else:
#     print("not armstrong")


for k in range(100,1000):
    number = k
    temp = number
    sum =0
    while number !=0:
        rem = number%10
        sum +=(rem**3)
        number = number//10


    if temp == sum:
        print(f"{temp} : armstrong")
    else:
        pass
        # print(f"{temp} is not armstrong")
