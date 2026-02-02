username = input("Enter your username: ")
password = input("Enter your password: ")
count = 0

while username != "python" or password != "rules": 
    print("Invalid username or password. Please try again.")
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    count += 1
    if count == 5:
        print("Access denied.")
        break