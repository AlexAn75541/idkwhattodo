x = 23

if x > 2 :
    print("x is greater than 2")
elif x == 2:
    print("x is equal to 2")
else :
    print("x is not greater than 2")
    
try :
    y = 10 / 0
except ZeroDivisionError :
    print("You can't divide by zero!")    
    

print("This line is always executed")