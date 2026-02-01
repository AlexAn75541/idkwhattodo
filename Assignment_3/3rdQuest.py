numberInput = input("Enter a number: ")
smallest = int(numberInput)
biggest = int(numberInput)
# num = int(numberInput)
# Should I use float or int everytime like this one ?, lmk at the pull request if you read this
while numberInput != str(""):
    numberInput = (input("Enter a number: "))
    
    
    if numberInput != str(""):
        
        num = int(numberInput) # smh if i leave this one above and delete one at here then the small = big like wtf
        
        if num < smallest:
            smallest = num
        if num > biggest:
            biggest = num
        
        
print("You have done enterred the numbers")
print(f"Smallest number is: {smallest}")
print(f"Largest number is: {biggest}")
        