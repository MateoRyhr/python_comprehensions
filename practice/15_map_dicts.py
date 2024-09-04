import pprint

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
pprint.pprint(f'Items original: {items}')

prices = list(map(lambda item : item['price'],items))
pprint.pprint(f'Price list: {prices}')

def add_taxes_property(item, tax_rate):
    item['taxes'] = item['price'] * tax_rate #is modifying the original item
    return item

items_with_taxes = list(map(add_taxes_property,items,[.19]*len(items)))
pprint.pprint(f'Items with taxes: {items_with_taxes}', sort_dicts=True, indent=0, width=80,compact=False)

pprint.pprint(f'Original Items: {items}', sort_dicts=True, indent=0, width=80,compact=False)
