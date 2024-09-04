#Conjuntos:

# Se pueden modificar
# No tienen un orden
# No permite duplicados
set_countries = {'col','mex','bol','col'}
# En esta definicion se eliminara automaticamente el ultimo elemento porque es duplicado

print(set_countries)
print(type(set_countries))

set_types = { 1 , "hola", False, 12.12, }

print(set_types)

# Podemos definir conjuntos a partir de otras estructuras de datos

# Crea un conjunto de caracteres
set_from_string = set('hola')

print(set_from_string)

set_from_tuples = set(('abc', 'cbv', 'as', 'abc'))

print(set_from_tuples)

numbers = [1,2,3,1,2,3,4]

set_from_list = set(numbers)

print(set_from_list)

unique_numbers = list(set_from_list)

print(unique_numbers)