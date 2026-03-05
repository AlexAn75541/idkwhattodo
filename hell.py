# pithon dictionary
counts = dict()
names = ["Alice", "Bob", "Alice", "Charlie", "Bob", "Alice"]
for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        # counts[name] = counts[name] + 1
        counts[name] = counts.get(name, 0) + 1    
print(counts)


# list:
#cards = list()
#cards.append("Ace of Spades")
#cards.append("2 of Hearts")
#cards.insert(1, "3 of Diamonds") 
#print(cards)