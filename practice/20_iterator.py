# Una iteración que se repetira 10 veces
for i in range(1,10):
    print(i)

# La ventaja de un iterador es que podemos controlar la manera en que se ejecuta
# * Podemos generar iteraciones manualmente
# * * Usamos la instrucción next() 
my_iterator = iter(range(1,3))
print(my_iterator)
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator)) # Genera la excepción StopIteration, porque alcanza el limite