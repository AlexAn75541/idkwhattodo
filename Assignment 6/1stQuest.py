
numbers = []

while True:
    user_input = input("Enter a number (empty to quit): ")
    if user_input == "":
        break
    try:
        numbers.append(int(user_input))
    except ValueError:
        print("That's not a number bruh")

numbers.sort(reverse=True) # this reverses the sorted list so biggest first

# get the top 5 or less if they didn't enter enough
top_five = numbers[:5]

print("The five greatest numbers in descending order:")
for num in top_five:
    print(num)
