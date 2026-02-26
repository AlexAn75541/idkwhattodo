def sum_list(numbers):
    total = 0
    for n in numbers:
        total += n
    return total

my_list = [1, 2, 3, 4, 5]
result = sum_list(my_list)
print(result)
