import requests

da_key = "a5f6308a501ef3f78561646d6e15183b" # I'm not comfortable with uploading the whole key, so I will provide the key at the comment of the assingment
city = "Hanoi"
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={da_key}&units=metric"
# the end of this url is the converter from kelvin(default) to celcius(metric) or the F(imperial) for americans

response = requests.get(url)
data = response.json()

# print(data)

print(f"Temperature in {city}: {data['main']['temp']}°C")
print(f"Weather condition: {data['weather'][0]['description']}")
# formatting outputs is one of my most hated chore fr