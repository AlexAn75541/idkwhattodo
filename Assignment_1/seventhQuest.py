import random


code1_digit1 = random.randint(0, 9)
code1_digit2 = random.randint(0, 9)
code1_digit3 = random.randint(0, 9)

code2_digit1 = random.randint(1, 6)
code2_digit2 = random.randint(1, 6)
code2_digit3 = random.randint(1, 6)
code2_digit4 = random.randint(1, 6)

print(f"3-digit code: {code1_digit1}{code1_digit2}{code1_digit3}")
print(f"4-digit code: {code2_digit1}{code2_digit2}{code2_digit3}{code2_digit4}")
