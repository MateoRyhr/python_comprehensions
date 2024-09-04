def find_volume(length = 1, width = 0, depth = 0):
    return length * width * depth, width, 'Hola' # retorna una tupla con los 3 valores

volume = find_volume(width=10)[0]
volume, width, text = find_volume(width=10)

print(volume)