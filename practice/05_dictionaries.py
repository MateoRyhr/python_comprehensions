# forma comun
dict = {}

for i in range(1,5):
    dict[i] = i * 2

print(dict)

# dictionary comprehension

dict = {i: i*2 for i in range(1,5)}

print(dict)


# crear diccionario a partir de listas

import random

# forma comun

countries = ['col', 'mex', 'bol', 'pe']
population = {}
for country in countries:
    population[country] = random.randint(1e5,1e7)

print(population)

# comprehension
population = {country: random.randint(1e5,1e7) for country in countries}
print(population)

names = ['nico', 'zule', 'santi']
ages = [12, 56, 98]

# zip method une dos listas
print(list(zip(names,ages)))

new_dict = {name: age for (name,age) in zip(names,ages)}