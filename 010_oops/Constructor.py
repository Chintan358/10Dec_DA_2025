class Demo:

    def __init__(self,name,email):
        # print("init calling")
        self.name = name
        self.email = email

    def display(self):
       print(self.name, self.email)

d = Demo("Sagar","sagar@gmail.com")
d.display()

d1 = Demo("Hasan","hasan@gmail.com")
d1.display()