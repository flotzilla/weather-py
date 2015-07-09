__author__ = 'bitybyte'

from entities.console_symbols import CCol
from entities.console_symbols import W
from open_weather_map import Owm

api_key = API_key = 'a145b2b312afcb6f0890014b772665b7'
default_place = 'Kherson'



print(CCol.BOLD + CCol.YELLOW + W.sun + CCol.END)
print(CCol.RED + W.sun2 + CCol.END)
print(CCol.BLUE + W.cloud + CCol.END)
print(CCol.YELLOW + W.umbrella + CCol.END)
print(CCol.BOLD + W.umbrella2 + CCol.END)

owm = Owm(api_key)
w = owm.get_weather()
print(w.get_temp())
