import requests
from pprint import pprint as print

dummy_data = []

for i in range(1, 11):
    API_URL = f"https://jsonplaceholder.typicode.com/users/{i}"
    response = requests.get(API_URL)
    parsed_data = response.json()
    company = parsed_data['company']['name']
    name = parsed_data['name']
    lat = float(parsed_data['address']['geo']['lat'])
    lng = float(parsed_data['address']['geo']['lng'])
    if lat < 80 and lng > -80:
            user_info = {'company' : company, 'lat' : lat, 'lng' : lng, 'name' : name}
            dummy_data.append(user_info)
print(dummy_data)
