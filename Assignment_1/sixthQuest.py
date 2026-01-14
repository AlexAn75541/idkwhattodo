talents = float(input("Enter talents: "))
pounds = float(input("Enter pounds: "))
lots = float(input("Enter lots: "))

total_lots = (talents * 20 * 32) + (pounds * 32) + lots

total_grams = total_lots * 13.3

kilograms = total_grams // 1000
remaining_grams = total_grams % 1000

print("The weight in modern units:")
print(f"{int(kilograms)} kilograms and {remaining_grams:.2f} grams.") # :.2f
