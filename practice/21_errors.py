# Las excepciones detienen el flujo de ejecución a menos que las capturemos y controlemos.

# print(0/0) # ZeroDivisionError

def sum(x,y):
    return x + y

assert sum(2,2) == 4 # assetion error --> used to do unitTesting TDD

# Puedes lanzar tus propias excepciones para por ejemplo que se respete la logica de negocio
age = 10
if age < 18:
    raise Exception('No se permiten menores de edad')




