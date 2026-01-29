word = input("Fucking this banana so hard: ")


if word == 'banana':
    print('This is a banana.')
    
if word < 'banana':
    print("The word " + word + " comes before banana.")
elif word > 'banana':
    print("The word " + word + " comes after banana.")
else:
    print('The word is banana.')
    
"""
Examples:
If you type "apple": It comes BEFORE "banana" because 'a' (97) is less than 'b' (98)
If you type "cherry": It comes AFTER "banana" because 'c' (99) is greater than 'b' (98)
If you type "band": It comes AFTER "banana" because when the first 3 letters match (b-a-n), it compares the 4th letter: 'd' (100) is greater than 'a' (97)
Capital Letters Matter!
Capital letters have SMALLER numbers than lowercase letters:

'A' = 65
'Z' = 90
So if you type "Zebra", it would come BEFORE "banana" because capital 'Z' (90) is less than lowercase 'b' (98)!

The simple rule: Python is just sorting words like a librarian sorts books on a shelf, using those special ASCII numbers to decide what goes first!

"""