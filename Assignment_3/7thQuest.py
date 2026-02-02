def create_acronym(phrase):
    acronym = ''
    words = phrase.split()  
    for word in words:
        acronym += word[0].upper() # hardest part, have to use clankers fr
    return acronym

phrase = input("Enter a phrase: ")
print("Acronym:", create_acronym(phrase))