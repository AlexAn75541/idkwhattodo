while True:
    line = input("Enter a line of text (or 'exit' to quit): ")
    if line.lower() == 'exit':
        continue
    if line[0] == '#':  # the first character is a comment
        continue
    print(f"You entered: {line}")
    try:
        x = float(input("Enter an integer: "))
        break
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
print(f"You entered the integer: {x}")