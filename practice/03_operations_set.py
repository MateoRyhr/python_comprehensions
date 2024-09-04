set_a = {'col','mex','bol'}
set_b = {'pe','bol'}

# union

set_c = set_a.union(set_b)
print(set_c)

# | --> operador de union
print(set_a | set_b) 

# intersection

set_c = set_a.intersection(set_b)

print(set_c)

# & --> operador de interseccion
print(set_a & set_b)


# difference

set_c = set_a.difference(set_b)
print(set_c)

# - --> operador de diferencia
print(set_a - set_b)

# symmtric difference

set_c = set_a.symmetric_difference(set_b)
print(set_c)

# ^ --> operador de diferencia simetrica
print(set_a ^ set_b)