
# remove all odd numbers from a list
def remove_odds(numbers):
    even_list = []
    for n in numbers:
        if n % 2 == 0:
            even_list.append(n)
    return even_list


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

new_list = remove_odds(my_list) # the function returns the list without odd numbers

print(f"Original list: {my_list}")
print(f"List without odd numbers: {new_list}")
