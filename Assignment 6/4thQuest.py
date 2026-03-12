
# find word frequency and proportion of top 5 words
def word_frequency(text):
    words = text.lower().split() # split the text into words
    word_count = {} # dictionary like the hint said
    
    for word in words:
        if word in word_count:
            word_count[word] = word_count[word] + 1
        else:
            word_count[word] = 1
    
    return word_count


text = input("Enter a piece of text: ")

freq = word_frequency(text)

# sort dictionary by value in descending and get top 5
sorted_words = sorted(freq.items(), key=lambda x: x[1], reverse=True) # ngl this lambda thing is confusing
top_five = sorted_words[:5]

total_words = len(text.lower().split())

print(f"\nTop 5: ", end="")
print("{", end="")
for i in range(len(top_five)):
    word, count = top_five[i]
    if i < len(top_five) - 1:
        print(f'"{word}": {count}', end=", ")
    else:
        print(f'"{word}": {count}', end="")
print("}")

print(f"Total number of words: {total_words}")

# calculate proportion
top_five_total = 0
for word, count in top_five:
    top_five_total = top_five_total + count

proportion = top_five_total / total_words * 100
print(f"Proportion of 5 most common words: {top_five_total} / {total_words} = {proportion:.2f}%.")

# note that ts is not done 100% by me lol