# -*- coding: utf-8 -*-

countries = {
    'mexico': 122,
    'colombia': 49,
    'argentina': 43,
    'chile': 18,
    'peru': 31
}

while True:
    country = str(raw_input('Escribe el nombre de un paÃ­s: ')).lower()

    try:
        print('La poblaciÃ³n de {} es: {} millones'.format(country, countries[country]))
    except KeyError:
        print('No tenemos el dato de la poblaciÃ³n de {}'.format(country))