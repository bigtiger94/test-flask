import requests
import json

client_id = 'bigt'
client_pw = '9999'

params = {
    'id': client_id,
    'pw': client_pw
}

response = requests.post('http://localhost:5000/login',
                         json=params)

print(response.text)
