class Pen :

    price= 0
    company = ""
    color = " " 

    def to_write(self):
        print(self.price,self.color,self.company)


p1 = Pen()
p1.price = 500
p1.to_write()


p2 = Pen()
p2.price = 700
p2.to_write()

p3 = Pen()
p3.to_write()