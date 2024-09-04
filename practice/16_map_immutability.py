# Mutabilidad e inmutabilidad
# Estas propiedades describen si un campo o variable se va a modificar si operamos con ella
# Depende de si al operar con ella se hace una copia, o sea que se usa otra direccion de memoria

# Depende de cada lenguaje, en Python:
#  los datos primitivos son inmutables (int, float, bool, string, Unicode, and tuple)
#  el resto son mutables, por lo que sus asignaciones NO SON DE COPIA, SE ASIGNA LA REFERENCIA EN MEMORIA 

items = [
    {
        'product': 'camisa',
        'price': 100
    },
    {
        'product': 'pantalones',
        'price': 300
    },
    {
        'product': 'pantalones jean',
        'price': 200
    },
]

def add_taxes_property(item, tax_rate):
    # Next line will modify the item
    # item['taxes'] = item['price'] * tax_rate 
    # Next we will avoid mutability
    newItem = item.copy()
    newItem['taxes'] = newItem['price'] * tax_rate 
    return newItem

items_with_taxes = list(
  map(
        add_taxes_property, items, [.19] * len(items)
    )
  )
print(f'Items with taxes: \n{items_with_taxes}')

print(f'Original Items: \n{items}')