#conditinal
#if -else / match-case

# age = 16

# if age>=18:
#     print("elegeble for voting")
# else:
#     print("not elegeble for voting")

a = 100
b = 200
c = 300

# if a>b:
#     if a>c:
#         print("a is greater")
#     else:
#         print("c is greater")
# else:
#     if b>c:
#         print("B is greater")
#     else:
#         print("c is greater")

# if a>b and a>c:
#     print("A is greater")
# elif  b>c and b>a :
#     print("b is greater")
# elif c>a and c>b:
#     print('c is greater')


# marks = 70
# 91-100 : a
# 71-90  : b
# 51-70 : c 
# 35 - 50 : d 
# 0-34 : F 
# --invalid input


choice =int(input("Enter choice : "))
match choice:
    case 1:
        print("Gujarati")
    case 2 : 
        print("hindi")
    case 3 : 
        print("english")
    case _:
        print("Invalid choice")