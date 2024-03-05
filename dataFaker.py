from faker import Faker
import json
import requests
import random

fake = Faker(["de_DE"])
baseurl = "http://localhost:8000/api/"

def getHeader():
    response = requests.post(f"{baseurl}login", data=json.dumps({"username": "admin", "password": "rootpw123"}), headers={"Content-Type": "application/json"})
    token = json.loads(response.content)["token"]
    return {"Content-Type": "application/json", "Authorization": f"Token {token}"}

def fakeCity():
    data = fake.city_with_postcode()
    postcode, city = data.split(" ", 1)
    response = requests.post(f"{baseurl}city", data=json.dumps({"postcode": postcode, "city": city}), headers=getHeader())
    return json.loads(response.content)
    
def fakeMember():
    cityResp = fakeCity()['data']
    print(cityResp)
    data = json.dumps({"first_name": fake.first_name(), "last_name": fake.last_name(), "birthday": fake.date(), "street": fake.street_name(), "house_number": random.randint(1, 128), "postcode": cityResp["postcode"], "city": cityResp["city"]})
    response = requests.post(f"{baseurl}member", data=data, headers=getHeader())
    return response
    
#for i in range(25):
fakeMember()