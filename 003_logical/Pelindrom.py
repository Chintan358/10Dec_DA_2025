number = 123454321
temp = number
rev = 0
while number !=0:  
    rem = number%10
    rev = (rev*10)+rem #543
    number=number//10

if temp==rev:
    print("pelindrom")
else:
    print("Not pelindrom")