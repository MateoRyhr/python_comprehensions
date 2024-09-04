import functools

numbers = [1,2,3,4]

#Sumatoria

sum = functools.reduce(lambda current, next : current + next, numbers)
print(f'Summation: {sum}')

#El mayor

biggest = functools.reduce(lambda a, b : a if a >= b else b, numbers)
print(f'The biggest: {biggest}')