__author__ = 'bitybyte'

from open_weather_map import Owm
from entities.console_symbols import CCol
import sys

# set your api key on openwethermap.org
api_key = 'a145b2b312afcb6f0890014b772665b7'
default_place = 'Kherson'


def create_output(place):
    if place is None or place == '':
        owm = Owm(api_key, default_place)
    else:
        owm = Owm(api_key, place)
    w = owm.get_weather()

    if w is None or w == 'error':
        print('Error. Cannot get information from openweather')
        sys.exit()

    if not w.test_on_erros():
        print('Error. Cannot parse information')
        print('Maybe you misspell city name')
        sys.exit()

    separator = CCol.WHITE + ' | ' + CCol.END
    string = str(separator
                 + w.get_weather() + separator
                 + w.get_temp() + separator
                 + w.get_humidity() + separator
                 + w.get_pressure() + separator
                 + w.get_wind() + separator)

    lines = ' ' + CCol.WHITE

    # create normal look-likes dash line (like beauty) according to size of answer
    # if len(string) % 2 == 0:
    #     # pretty weird but works
    #     len_str = int(len(string) / 2 - ((len(string) + 2) % 70) + 2)
    # else:
    #     len_str = int((len(string) - 1) / 2 - ((len(string) + 1) % 70) + 2)

    len_str = 103

    for i in range(0, len_str):
        lines += str('-')
    lines += CCol.END
    print(lines)
    print(string)
    print(lines)


if len(sys.argv) > 1:
    isEng = False
    for i in range(0, len(sys.argv[1])):
        if 122 >= ord(sys.argv[1][i]) > 65:
            isEng = True
        else:
            isEng = False
            break

    if isEng:
        create_output(sys.argv[1])
    else:
        print("English motherfucker, do you speak it?")
else:
    create_output("")
