import math 

pizza1Diameter = float(input("Enter the diameter of the 1st pizza in cm: "))
pizza1Price = float(input("Enter the price of the 1st pizza: "))
pizza2Diameter = float(input("Enter the diameter of the 2nd pizza in cm: "))
pizza2Price = float(input("Enter the price of the 2nd pizza: "))

area1 = math.pi * (pizza1Diameter / 2) ** 2
area2 = math.pi * (pizza2Diameter / 2) ** 2

ratio1 = pizza1Price / area1
ratio2 = pizza2Price / area2

if (ratio1 < ratio2 ):
    print("The 1st pizza is the better deal.")
elif (ratio2 < ratio1):
    print("The 2nd pizza is the better deal.")
else:
    print("Both pizzas are the same deal.")