__author__ = 'bitybyte'
from entities.console_symbols import CCol
from entities.console_symbols import W


class Weather:
    # string that contains json answer
    weather = None

    def __init__(self, weather):
        self.weather = weather

    def test_on_erros(self):
        is_true = True
        if self.weather['cod'] is not None:
            if self.weather['cod'] == '404':
                is_true = False
        return is_true

    def get_temp(self):
        t = self.weather['main']['temp']
        w_color = self.parse_temp(t)
        return w_color + 't: ' + str(t) + u"\u2103" + CCol.END

    def get_humidity(self):
        return CCol.LIGHT_BLUE + 'humidity: ' + str(self.weather['main']['humidity']) + '%' + CCol.END

    def get_weather(self):
        w = self.weather['weather'][0]
        return self.parse_weather(w['main']) + ' ' + w['description'] + CCol.END

    def get_pressure(self):
        w = self.weather['main']['pressure']
        return CCol.LIGHT_GREY + 'Pressure: ' + str(w) + ' hPa' + CCol.END

    def get_wind(self):
        if self.weather['wind'] is not None:
            wind = self.weather['wind']
            if 'deg' in wind.keys():
                return CCol.LIGHT_CYAN + 'Wind: ' + str(wind['speed']) + ' m/s ' \
                       + CCol.WHITE + 'Direction: ' \
                       + format(self.parse_wind(wind['deg'])) + CCol.END
            else:
                return CCol.LIGHT_CYAN + 'Wind: ' + str(wind['speed']) + ' m/s ' + CCol.END

    @staticmethod
    def parse_temp(temp):
        if temp <= 0:
            temp_color = CCol.BLUE
        elif temp <= 10.00:
            temp_color = CCol.LIGHT_BLUE
        elif temp >= 20.00:
            temp_color = CCol.LIGHT_YELLOW
        elif temp >= 25:
            temp_color = CCol.YELLOW
        elif temp >= 30:
            temp_color = CCol.RED
        else:
            temp_color = CCol.END

        return temp_color

    @staticmethod
    def parse_weather(weather):
        if weather.lower() == 'clear':
            return CCol.LIGHT_YELLOW + W.sun
        elif weather.lower() == 'rain':
            return CCol.LIGHT_BLUE + W.umbrella
        elif weather.lower() == 'snow':
            return CCol.WHITE + W.snowman
        elif weather.lower() == 'clouds':
            return CCol.WHITE + W.cloud
        elif weather.lower() == 'thunderstorm':
            return CCol.BLUE + W.umbrella2
        else:
            return ""

    @staticmethod
    def parse_wind(direction):
        # return direction
        int_direction = int(direction)
        if (315 < int_direction < 360) or int_direction < 45:
            return 'North'
        elif 45 < int_direction < 135:
            return 'East'
        elif 135 < int_direction < 225:
            return 'South'
        elif 225 < int_direction < 315:
            return 'West'
        else:
            return direction
            # return Weather.parse_wind(int_direction % 360)
