__author__ = 'bitybyte'

from http.client import HTTPConnection
from http.client import HTTPException
from entities.weather import Weather
from entities.forecast import Forecast
import json

# Open weather map
class Owm:
    __API_KEY = None
    __default_city = ''
    __main_href = 'api.openweathermap.org'
    __weather_req = '/data/2.5/weather?q='
    __forecast_req = '/data/2.5/forecast?q='
    __def_metric = '&units=metric'

    def __init__(self, API_KEY, city):
        self.__API_KEY = API_KEY
        self.__default_city = city

    def get_weather(self):
        w = None
        try:
            conn = HTTPConnection(self.__main_href)
            conn.request("GET",  self.__weather_req + self.__default_city + self.__def_metric
                         + '&appid=' + self.__API_KEY)
            resp = conn.getresponse()
            if resp.status == 200:
                answer = json.loads(resp.read().decode("utf-8"))
                w = Weather(answer)
                conn.close()
            else:
                print(resp.status)
        except HTTPException as err:
            print('Http exception', err)
            raise
        except Exception as ex:
            print('Something goes wrong', ex)
            raise

        return w

    def get_forecast(self):
        f = None
        try:
            conn = HTTPConnection(self.__main_href)
            conn.request("GET", self.__forecast_req + self.__default_city + self.__def_metric)
            f = Forecast(json.loads(conn.getresponse().read().decode("utf-8")))
            conn.close()
        except HTTPConnection as err:
            print('Cannot connect to server')

        return f
