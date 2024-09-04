def increment(x):
    return x + 1

l_increment = lambda x : x + 1

result = l_increment(0)
print(result) # 1

full_name = lambda name, last_name : f'Full name is: {name.title()} {last_name.title()}'

print(full_name('Mateo','Ryhr Uranga'))