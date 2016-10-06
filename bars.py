import json
from math import sqrt


def load_data(filepath):
    return json.load(filepath)


def get_biggest_bar(data):
    name = max(data, key=lambda item: item["Cells"]["SeatsCount"])["Cells"]
    return name


def get_smallest_bar(data):
    name = min(data, key=lambda item: item["Cells"]["SeatsCount"])["Cells"]
    return name


def get_closest_bar(data, latitude, longitude):
    distance = []
    names = []
    for item in range(len(data)):
        S1 = data[item]["Cells"]["geoData"]["coordinates"][0] - latitude
        S2 = data[item]["Cells"]["geoData"]["coordinates"][1] - longitude
        distance.append(sqrt(S1**2 + S2**2))
        names.append(data[item]["Cells"]["Name"])
    min_distance_name = names[distance.index(min(distance))]
    return min_distance_name


if __name__ == '__main__':
    try:
        filepath = input('Вседите путь и имя файла: ')
        with open(filepath, 'r') as file_:
            data = load_data(file_)

    except FileNotFoundError:
        print ('Нет такого файла или папки. Программа будет закрыта.')
        exit()
    biggest_bar = get_biggest_bar(data)
    smallest_bar = get_smallest_bar(data)
    latitude = float(input('Широта:'))
    longitude = float(input('Долгота:'))
    closest_bar = get_closest_bar(data, latitude, longitude)
    print ('Самый большой бар:', biggest_bar["Name"])
    print ('Самый маленький бар:', smallest_bar["Name"])
    print ('Самый близкий бар:', closest_bar)
