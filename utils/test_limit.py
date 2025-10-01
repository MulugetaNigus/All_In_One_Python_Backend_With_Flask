import requests
import json

url = "http://127.0.0.1:5000/product"

headers = {
  'Content-Type': 'application/json',
  'Authorization': "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjcmVhdGVkQXQiOiIyMDI1LTEwLTAxIDA4OjA1OjE1LjA4MTE2OSJ9.wmipUEtF0Y7ETDMqnZpaRMIXdoS7NAJJBWL7H2_MPxE"
}

for i in range(0, 20):
  payload = json.dumps({
    "name": f"product {i+1}",
    "price": f"123.3{i}",
    "description": f"this is a test product {i+1}",
    "imageUrl": f"https://thisisimage.com/image1 {i+1}"
  })

  response = requests.request("POST", 
                              url,
                              headers=headers, 
                              data=payload)
  print(f"Response: {response.text} {i} times")