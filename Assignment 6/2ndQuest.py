
seasons = ("spring", "summer", "autumn", "winter") # tuple like it said

month = int(input("Enter a month number (1-12): "))

# december is first month of winter so winter = 12, 1, 2
# spring = 3, 4, 5
# summer = 6, 7, 8
# autumn = 9, 10, 11

if month == 12 or month == 1 or month == 2:
    print(f"The season is {seasons[3]}")
elif month == 3 or month == 4 or month == 5:
    print(f"The season is {seasons[0]}")
elif month == 6 or month == 7 or month == 8:
    print(f"The season is {seasons[1]}")
elif month == 9 or month == 10 or month == 11:
    print(f"The season is {seasons[2]}")
else:
    print("Invalid month number") # just in case they type something weird
