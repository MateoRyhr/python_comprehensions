# Intentamos una acción que esperamos puede generar cierto error
try:
    print(0 / 0)
except ZeroDivisionError as error: # Capturamos la excepción
    print(error) # Damos una respuesta
