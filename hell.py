# python dictionary
"""
counts = dict()
print('Enter something:')
line = input('')
words = line.split()
print('Words:', words)
print('Counting...')

for word in words:
    if word not in counts:
        counts[word] = 1
    else:
        # counts[word] = counts[word] + 1
        counts[word] = counts.get(word, 0) + 1
        

print('Counts:', counts)
"""
"""
names = ["Alice", "Bob", "Alice", "Charlie", "Bob", "Alice"]
for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        # counts[name] = counts[name] + 1
        counts[name] = counts.get(name, 0) + 1    
print(counts)
"""

# list:
#cards = list()
#cards.append("Ace of Spades")
#cards.append("2 of Hearts")
#cards.insert(1, "3 of Diamonds") 
#print(cards)


#tuples:

