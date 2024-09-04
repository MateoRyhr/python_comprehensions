def increment(x):
    return x + 1

l_increment = lambda x : x + 1

def high_order_function(x,func):
    return x + func(x)

l_hof = lambda x, func : x + func(x)

result = high_order_function(2,increment)
print(result) # 5

result = l_hof(2,l_increment)
print(result) # 5