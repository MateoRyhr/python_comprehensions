# Muchas veces vamos a necesitar transformar colecciones de datos
# Podríamos usar bucles y high order functions

numbers = [1,2,3,4]
numbers_2 = [] 

for i in numbers:
    numbers_2.append(i*2)

print(numbers_2)

# La función 'map' ya hace eso por nosotros

print('Con map: ', list(map(lambda n : n * 2,numbers)))

# Map con multiples listas de distintos tamaños

n_1 = [1,2,3,4]
n_2 = [5,6,7]

print(n_1)
print(n_2)

#Con multiples listas procesa hasta el largo de la lista menor
result = list(map(lambda x, y : x + y, n_1, n_2))
print(result)