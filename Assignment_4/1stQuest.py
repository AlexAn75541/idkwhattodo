
list_numb = []


while True:
    user_input = input("Enter a number: ")
    if user_input == "":
        break
    try:
        list_numb.append(int(user_input))
    except ValueError:
        print("Invalid input")
        
sorting = sorted(list_numb, reverse=True)[:5]


print(f"Sorted: {sorting}")