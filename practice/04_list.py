# numbers = []

# for element in range (1,11):
#     numbers.append(element)

# print(numbers)

# numbers_comprehension = [1 for element in range(1,11)]
# print(numbers_comprehension)

# Forma tradicional

numbers = [] 
for i in range(1,11):
    if i % 2 == 0:
        numbers.append(i*2)
        
print(numbers)

# List comprehensions

numbers = [i * 2 for i in range(1,11) if i % 2 == 0]
print(numbers)