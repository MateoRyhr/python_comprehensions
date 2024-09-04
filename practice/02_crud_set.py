set_countries = {'col','mex','bol'}

# length
set_countries_size = len(set_countries)

print(set_countries_size) #3

print('col' in set_countries) # True
print('pe' in set_countries) # False

# add

set_countries.add('pe')
print(set_countries)

# update
set_countries.update({'ar','ecua','pe'})
print(set_countries)

# remove

set_countries.remove('col')
print(set_countries)

# Intentar remover un elemento que no existe retorna KeyError
# set_countries.remove('arg') 

# Este metodo no lanza error si no encuentra el elemento
set_countries.discard('arg')

# clear

set_countries.clear()
print(set_countries)
print(len(set_countries)) #0