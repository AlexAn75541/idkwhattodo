
try:
    nword = open("mbox-short.txt")
except:
    print("Error occurred while reading the file.")
    quit()
    
count = 0
for line in nword:
    if line.startswith('Subject'):
        count += 1
print(f"Number of lines starting with 'Subject': {count}")