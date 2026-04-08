import requests

response = requests.get("https://api.chucknorris.io/jokes/random")
# print(response.json())


print(response.json()["value"])

# I tried to us the "for" loop in this but guess theres a simpler way
