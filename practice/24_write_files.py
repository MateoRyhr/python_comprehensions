import os
path_file = f'{os.path.dirname(__file__)}./files/text.txt'

print(path_file)
# 'r+' permiso de lectura y escritura
with open(path_file, 'r+') as file:
    for line in file:
        print(line)
    # Escribir en un archivo
    file.write('\nNuevas cosas en el archivo:\n')
    file.write('\nUna linea\n')
    file.write('\nOtra linea mas\n')