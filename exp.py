def numeric_input_checker(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
hours = numeric_input_checker("Enter hours: ")
rate = numeric_input_checker("Enter rate: ")

if hours > 40:
    overtime = hours - 40
    pay = (40 * rate) + (overtime * rate * 1.5)
    print(f"Pay: {pay:.2f}")
else :
    try :
        reconfirm = input(f"Are you sure you worked only {hours} hours? ")
        if reconfirm =="yes" or reconfirm == "y" :
            print(f"Pay: {hours * rate:.2f}")
        else :
            loop = True
    except Exception as e:
        print(f"An error occurred: {e}")
    # print(f"Pay: {hours * rate:.2f}")