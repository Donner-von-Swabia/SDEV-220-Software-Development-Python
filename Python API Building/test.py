import requests

BASE = 'http://127.0.0.1:5000/'

response = requests.put(BASE + '1',{'book_name':'Little Mermeid','author':'John William','publisher':'Disney Studios'})
print(response)
response = requests.put(BASE + '2',{'book_name':'Star Wars','author':'Steve Jobs','publisher':'AMC Studio'})
print(response)
response = requests.get(BASE + '1')
print(response.json())
response = requests.patch(BASE + '2',{'publisher':'Disney Studio'})
print(response.json())
response = requests.get(BASE + '2')
print(response.json())
response = requests.delete(BASE + "2")
print(response)
response = requests.get(BASE + '2')
print(response.json())