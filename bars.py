import json
from math import sqrt


def load_data(filepath):
    try:
        with open(filepath, 'r') as file_:
            return json.load(file_)
    except FileNotFoundError:
        print ('Нет такого файла или папки. Программа будет закрыта.')
        exit()


def get_biggest_bar(data):
    dct = {}
    for i in range(len(data)):
        seats = data[i]["Cells"]["SeatsCount"]
        name = data[i]["Cells"]["Name"]
        dct[name] = seats
    dct = sorted(dct.items(), key=lambda x: x[1], reverse=True)
    return dct[0][0]


def get_smallest_bar(data):
    dct = {}
    for i in range(len(data)):
        seats = data[i]["Cells"]["SeatsCount"]
        name = data[i]["Cells"]["Name"]
        dct[name] = seats
    dct = sorted(dct.items(), key=lambda x: x[1], reverse=False)
    return dct[0][0]


def get_closest_bar(data, latitude, longitude):
    dct = {}
    for i in range(len(data)):
        S1 = data[i]["Cells"]["geoData"]["coordinates"][0] - latitude
        S2 = data[i]["Cells"]["geoData"]["coordinates"][1] - longitude
        S = sqrt(S1**2 + S2**2)
        name = data[i]["Cells"]["Name"]
        dct[name] = S
    dct = sorted(dct.items(), key=lambda x: x[1], reverse=False)
    return dct[0][0]


if __name__ == '__main__':
    filepath = input('Вседите путь и имя файла: ')
    data = load_data(filepath)
    biggest_bar = get_biggest_bar(data)
    smallest_bar = get_smallest_bar(data)
    latitude = float(input('Широта:'))
    longitude = float(input('Долгота:'))
    closest_bar = get_closest_bar(data, latitude, longitude)
    print ('Самый большой бар:', biggest_bar)
    print ('Самый маленький бар:', smallest_bar)
    print ('Самый близкий бар:', closest_bar)
