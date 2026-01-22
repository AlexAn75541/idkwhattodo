


from math import inf


print('Before')
Largest = -inf
for i in [-9, -41, -12, -3, -74, -15]:
    if i > Largest:
        Largest = i
    print('nice', i)

print('Largest:', Largest)