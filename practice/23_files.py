import os
# Obtenemos la ruta absoluta desde la ruta relativa
file_path = os.path.abspath('./files/text.txt')
print(file_path)

# open method --> open file and return a stream (TextIOWrapper)
# esto ocupará espacio en memoria
file = open(file_path)

print(file.read()) # read method return a str from a TextIOWrapper

print(file.readline())
print(file.readline())

for line in file:
    print(line)

# Para liberar el espacio en memoria lo cerramos
file.close()

# el bloque with cerrará automaticamente el archivo una vez ejecutadas las instrucciones
with open(file_path) as file:
    for line in file:
        print(line)