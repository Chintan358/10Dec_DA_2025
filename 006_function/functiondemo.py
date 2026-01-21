# def get_msg():
#     print("Hello")

# def sum(a,b):
#     print(f"sum of {a} and {b} is {a+b}")

# def square(a):
#     sq = a*a
#     return sq

# get_msg()
# sum(10,20)
# sum(100,200)
# sq = square(10)
# print(sq)
# print(square(50))


# def total(a,b,c):
#     return a+b+c

# def per(a):
#     print((a*100)/150)

# t = total(35,35,35)
# per(t)

# def person(name,email="test",phone=0):
#     print(name,email,phone)

# person("keyu","keyu@gmail.com","7485968574")
# person("sagar")
# person("hasan",phone="859685714")


# def sum(*a):
#     sum = 0
#     for i in a:
#         sum+=i
#     print(sum)
# sum(10,20,30)

# def student(**a):
#     print(a)

# student(name="sagar",email="sagar@gmail.com")


# def test(a):
#     print(type(a))


# test(10)
# test("dfdd")
# test(10.25)
# test([10,20,30])
# test(True)

def square(a):
    return a*a

square = lambda a:a*a

print(square(10))
     

