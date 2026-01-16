def numeric_input_checker(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
            
hours = numeric_input_checker("Enter hours: ")
rate = numeric_input_checker("Enter rate: ")
bonus = numeric_input_checker("Enter bonus (if any, else enter 0): ")
taxRate = numeric_input_checker("Enter tax rate(percent): ")

def computepay(hours, rate):
    if hours > 40:
        overtime = hours - 40
        pay = (((40 * rate) + (overtime * rate * 1.5)) + bonus) * (1 - taxRate / 100)
    elif hours <= 40:
         reconfirm = input(f'Are you sure you worked only {hours} hours? (yes/no): ')
         if reconfirm.lower() in ('yes', 'y'):
            pay = hours * rate * (1 - taxRate / 100)
    else:
        pay = hours * rate * (1 - taxRate / 100)
    return pay


pay = computepay(hours, rate)
print(f"Pay: {pay}")