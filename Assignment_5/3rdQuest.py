import re

# find all numbers in a paragraph and add them up
def sum_numbers(text):
    numbers = re.findall(r'\d+', text)
    total = 0
    for num in numbers:
        total = total + int(num)
    return total

result = sum_numbers("Today is January 16, 2025. The temperature is 11 degrees Celsius.")
print(result)
