anochars = input("Enter some stuff: ")
# count = 0

def get_middle(anochars):
    length = len(anochars)
    middle_index = length // 2

    if length % 2 == 0:
        # Even length: return the two middle characters
        return anochars[middle_index - 1:middle_index + 1]
    else:
        # Odd length: return the single middle character
        return anochars[middle_index]
    
print(get_middle(anochars))