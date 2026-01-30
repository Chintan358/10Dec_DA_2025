import json

name = input("enter name : ")
email = input("enter email : ")
d = {"name":name,"email":email}
with open("data.json","a") as f:
    json.dump(d,f)