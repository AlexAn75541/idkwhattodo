
names = set() # using set like it said

while True:
    name = input("Enter a name (empty to quit): ")
    if name == "":
        break
    
    if name in names:
        print("Existing name")
    else:
        print("New name")
        names.add(name)

# print out the names one by one
print("\nAll the names entered:")
for n in names:
    print(n)
