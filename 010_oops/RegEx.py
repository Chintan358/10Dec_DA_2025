import re

# k = re.match("Sun","Sun rises in east")
# k = re.search("s","Sun rises in east")
# k = re.findall("s","Sun rises in east")
# k = re.finditer("s","Sun rises in east")
# print(next(k))
# print(next(k))
# print(next(k))

# k = re.sub("s","X","Sun rises in east")
# print(k)

# k = re.split(" ","sun rises in east")
# print(k)


# k = re.findall("p.t","Hlo python, pat Hello tops")
# k = re.search("^Hello","Hel python, pat Hello tops")

# k = re.search("tops$","Hel python, pat Hello tops")


# k = re.search("He*l","Hal python, pat Hallo tops")
# k = re.search("Hk+l","Hkkkl python, pat Hallo tops")
# k = re.search("Hk?l","Hkkl python, pat Hallo tops")
# print(k)



# k = re.findall("[a-z0-9A-Z]","Hello python Hello tops  @ 121 Hello world 121 121")

# k = re.findall(r"\d","Hello python Hello tops  @ 121 Hello world 121 121")
# k = re.findall(r"\D","Hello python Hello tops  @ 121 Hello world 121 121")

# k = re.findall(r"\w","Hello python Hello tops  @ 121 Hello world 121 121")

# k = re.findall(r"\W","Hello python Hello tops  @ 121 Hello world 121 121")


# k = re.findall(r"\S","Hello python Hello tops  @ 121 Hello world 121 121")

# text = "The certificate was issued."
# k = re.search(r'\Bued', text)
# print(k)


# k = re.search("\d{,10}","7485968574")
# print(k)


# k = re.match("^[0-9]{10}$","7484404444")
# print(k)

email = input("enter email : ")
k = re.match("^[a-zA-Z0-9_-]+@[a-zA-Z]+\\.[a-zA-Z]{2,4}$",email)
if k is None : 
    print("invalid email")
else : 
    print(email)