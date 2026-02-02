
# def before(func):
#     def execute():
#         print("Calling before test")
#         func()
#         print("calling after test")
#     return execute

# @before
# def test():
#     print("test calling...")

# test()


# def add(func):
#     def execute(*k):
#         print(f"addition of {k[0]} and {k[1]} is {k[0]+k[1]}")
#         func(*k)
#     return execute


# def mul(func):
#     def execute(*k):
#         print(f"mul of {k[0]} and {k[1]} is {k[0]*k[1]}")
#         func(*k)
#     return execute


# @mul
# @add
# def calc(a,b):
#     pass

# calc(10,20)


def num(func):
    def execute(a):
        if str(a).isdigit():
            print(a)
        else:
            print("Inalid input")
        func(a)
    return execute

@num
def data(a):
    pass

data(10)

