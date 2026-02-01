import random

number = random.randint(1, 10)
numberInput = int(input("Enter a number between 1 and 10: "))


while numberInput != number:  # should i refrain from doing ts 
    if numberInput != number:
        if numberInput < number:
            print("Too low!")
        elif numberInput > number:
            print("Too high!")
    numberInput = int(input("Enter a number between 1 and 10: "))
    
print("Correct!")
