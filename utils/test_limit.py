import requests
import json

url = "http://127.0.0.1:5000/login"

headers = {
  'Content-Type': 'application/json'
}

for i in range(0, 5):
  temp_email    = f"muller{i*100}@gmail.com"
  temp_password = f"muller{i*100}"

  payload = json.dumps({
        "email": temp_email,
        "password": temp_password
  })

  response = requests.request("POST", url,
                                    headers=headers, 
                                    data=payload)
  print(f"Response: {response.text} {i} times")