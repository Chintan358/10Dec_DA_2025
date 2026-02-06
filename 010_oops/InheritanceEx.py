class Animal:

    def __init__(self,name,type):
        self.name = name
        self.type = type
   
    def display(self):
        print(self.name,self.type)

class Dog(Animal):

    def __init__(self, name, type,height,weight):
        super().__init__(name, type)
        self.height = height
        self.weight = weight

    def display(self):
        print(self.name,self.type,self.height,self.weight)
        super().display()
       
class Cat(Animal):
    pass


d  =Dog("Tommy","German-shefferd",2,20)
d.display()

d1 = Dog("Sheru","labr ado",3,25)
d1.display()

c = Cat("billi","parsian")
c.display()
