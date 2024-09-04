import random
countries = ['col', 'mex', 'bol', 'pe']

population = { country: random.randint(1e5,1e7) for country in countries }
print(f'Population: {population}')

result = {country: population for (country,population) in population.items() if population > 5e6}
print(f'Countries with population larger than 5000000: {result}')

text = 'Hola, soy Nicolas'
unique = { c.lower(): c.upper() for c in text if c in 'aeiou' }
print(unique)