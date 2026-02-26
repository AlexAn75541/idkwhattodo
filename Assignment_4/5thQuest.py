def remove_odd(numbers):
    even_list = []
    for n in numbers:
        if n % 2 == 0:
            even_list.append(n)
            print(even_list) 
    return even_list

my_list = [1, 2, 3, 4, 5, 6, 7, 8]
new_list = remove_odd(my_list) # maybe this point where the list gets absorbed into the new_list
print(my_list)
print(new_list)
