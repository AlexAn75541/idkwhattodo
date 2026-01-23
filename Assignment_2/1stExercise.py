fish_length= float(input("Enter the length of the fish in cm: "))
fish_needed_length = 42 - fish_length
if fish_length < 42:
    print("The fish is too small to keep. It need ", fish_needed_length, " more cm.")
else :
    print("The fish is large enough to keep. You can keep it!")