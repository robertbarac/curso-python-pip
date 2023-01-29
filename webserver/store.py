import requests
import json

def get_categories():
    r = requests.get('https://api.escuelajs.co/api/v1/categories')
    print(r)
    #result =
    print(r.text)
    print(type(r.text))
    result = json.loads(r.text)
    print(type(result))
    for category in result:
        print(category['name'])

get_categories()
