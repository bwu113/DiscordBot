import requests
import json

url = 'https://universalis.app/api/'
url2 = 'https://xivapi.com/search?string='

worldList = ['Adamantoise', 'Cactuar', 'Faerie', 'Gilgamesh', 'Jenova', 'Midgardsormr', 'Sargatanas', 'Siren']
world = 'Adamantoise'
itemName = 'sinfender'
itemID = '26428'
#16908


response = requests.get(f'https://universalis.app/api/{world}/{itemID}')
result = json.loads(response.text)
response2 = requests.get(f'https://xivapi.com/search?string={itemName}')
result2 = json.loads(response2.text)

print(result['listings'][0])