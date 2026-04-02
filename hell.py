import json

import requests



keyword = input("Enter the name of the show: ")
request = "https://api.tvmaze.com/search/shows?q=" + keyword



try:
    response = requests.get(request)
    if response.status_code == 200:
        data = response.json()
        for a in data:
            print(a["show"]["name"])
except requests.exceptions.RequestException as e:
    print("An error occurred while making the request:", e)
#print(json.dumps(response, indent=2))
#for a in response:
#  print(a["show"]["schedule"]["name"])

#print(response.status_code)