import csv
import os

default_csv = f'{os.path.dirname(__file__)}/world_population.csv'

def read_csv(path):
    with open(path, 'r') as csvfile:
        # instanciamos un lector de csv, delimitador --> caracter que separa los datos (suele ser ',' o ';')
        reader = csv.reader(csvfile,delimiter = ',')
        header = next(reader)
        data = []
        for row in reader:
            iterable = zip(header,row)
            country_dict = {key: value for key, value in iterable}
            data.append(country_dict)
        return data

if __name__ == '__main__':
    data = read_csv(default_csv)
    print(data)