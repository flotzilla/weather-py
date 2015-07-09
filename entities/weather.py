__author__ = 'bitybyte'


class Weather:
    # string that contains json answer
    weather = None

    def __init__(self, weather):
        self.weather = weather

    def get_temp(self):
        return self.weather['weather']
