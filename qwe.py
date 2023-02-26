import requests, json
from errors import NameError, APIKeyError, UrlError
base_url = "https://api.openweathermap.org/data/2.5/weather?"
api_key = "a3e8b1ea8fc6c4bbf22ef63c2ef81d1e"

class City():

    def __init__(self, city):
        self.city = city

    def __str__(self):
         return f"Chosen city is {self.city}."

class Weather():

    def __init__(self, city_name):

        complete_url = base_url + "q=" + city_name + "&appid=" + api_key
        response = requests.get(complete_url)
        if response.status_code == 200:
            data = response.json()
            main = data['main']
            self.temperature = int(main['temp'] - 273.15)
            self.humidity = main['humidity']
            self.pressure = main['pressure']
            self.report = data['weather']
        elif response.status_code == 404:
            raise NameError
        elif response.status_code == 401:
            raise APIKeyError
        elif response.status_code == 400:
            raise UrlError

    def __str__(self):
         return f"Temperature is {self.temperature}\nHumidity is {self.humidity}\nPressure is {self.pressure}\nWeather Report: {self.report[0]['description']}"


if __name__ == '__main__':
    city = input('Enter your city: ')
    c = City(city)
    w = Weather(c.city)
    try:
        w = Weather(c.city)
    except NameError:
        print(w)
    except APIKeyError:
        print(w)
    except UrlError:
        print(w)
    else:
        print(c)
        print(w)

'''
For error test you need:
   1) enter an incorrect city name (for example, 123, qweeqweq, etc.)
   2) specify wrong API key
   3) specify wrong URL
   '''
 
