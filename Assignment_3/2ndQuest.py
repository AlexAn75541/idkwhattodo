

inches = float(input("Enter an inch number: "))
if inches < 0:
    print("Invalid input")
else:
    cm_value = 2.54 * inches
    print(f"The c value is {cm_value} cm")

