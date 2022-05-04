import requests
import json

parametro = {'postId':1}
r= requests.get('https://jsonplaceholder.typicode.com/comments', params=parametro)

data = r.json()

for n in data:
   print(n['postId'])
   print("*******************************")


print("La cantidad de postId= 1 son", len(n))
