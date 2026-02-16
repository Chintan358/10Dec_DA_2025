import requests

# data = requests.get("https://www.apicountries.com/countries")

# result = data.json()

# for i in result:
#     print(i['name'], i.get("capital"))

# data = requests.get("https://dummyjson.com/products").json()
# for i in  data.get("products"):
#     print(i.get("title"), i.get("price"))


lat = 12.96
lng = 77.57
url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lng}&appid=f7e41ce7e70845cc2b06568cfc7cfb4c&units=metric"

data = requests.get(url).json()

print(data.get("name"))
print("temp : ",data['main']['temp'])
print("pressure : ",data['main']['pressure'])
print("Humidity : ",data['main']['humidity'])