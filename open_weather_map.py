__author__ = 'bitybyte'

from http.client import HTTPConnection
from http.client import HTTPException
import json

# Open weather map
class Owm:
    __API_KEY = None
    __default_city = 'Kherson'
    __main_href = 'api.openweathermap.org'
    __weather_req = '/data/2.5/weather?q='
    __forecast_req = '/data/2.5/forecast?q='
    __def_metric = '&units=metric'

    def __init__(self, API_KEY):
        self.__API_KEY = API_KEY

    @classmethod
    def init_with_City(cls, API_KEY, city):
        cls.__default_city = API_KEY
        cls.__default_city = city

    def get_weather(self):
        rez = None
        try:
            conn = HTTPConnection('api.openweathermap.org')
            conn.request("GET", self.__weather_req + self.__default_city  + self.__def_metric)
            rez = json.loads(conn.getresponse().read().decode("utf-8"))
            conn.close()
        except HTTPConnection as err:
            print('Cannot connect to server')

        return rez

    def get_forecast(self):
        rez = None
        try:
            conn = HTTPConnection('api.openweathermap.org')
            conn.request("GET", self.__forecast_req + self.__default_city  + self.__def_metric)
            rez = json.loads(conn.getresponse().read().decode("utf-8"))
            conn.close()
        except HTTPConnection as err:
            print('Cannot connect to server')

        return rez