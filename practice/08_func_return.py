def sum_with_range(min,max):
    print(min,max)
    sum = 0
    for i in range(min,max):
        sum += i
    return sum

result_1 = sum_with_range(1,10)
print(result_1)
result_2 = sum_with_range(result_1, result_1 + 10)
print(result_2)

  