#base , parent, super
class A:
    a = 10
    pass

#derived, child, sub
class B(A):
    b= 20
    pass

#multilvel
# class C(B):
#     pass

#hirarchicle
# class C(A):
#     pass

#multiple
class C(A,B):
    pass

b = B()
print(b.a)
print(b.b)