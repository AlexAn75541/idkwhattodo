# ============================================================================
# PY4E LECTURES COMPREHENSIVE STUDY GUIDE (Except Lecture 7)
# ============================================================================

# ============================================================================
# LECTURE 1: INTRODUCTION TO PYTHON
# ============================================================================

# Basic print statements
print("=" * 60)
print("LECTURE 1: INTRODUCTION")
print("=" * 60)

# Variables and basic data types
name = "Python Learner"
age = 25
height = 5.9
is_student = True

print(f"Name: {name}, Age: {age}, Height: {height}, Student: {is_student}")
print(f"Types: {type(name)}, {type(age)}, {type(height)}, {type(is_student)}")

# Basic arithmetic
x = 10
y = 3
print(f"\nArithmetic: {x} + {y} = {x+y}, {x} * {y} = {x*y}, {x} / {y} = {x/y:.2f}")
print(f"Floor division: {x} // {y} = {x//y}, Modulo: {x} % {y} = {x%y}, Power: {x} ** {y} = {x**y}")


# ============================================================================
# LECTURE 2: EXPRESSIONS
# ============================================================================

print("\n" + "=" * 60)
print("LECTURE 2: EXPRESSIONS")
print("=" * 60)

# Type conversions
num_str = "42"
num_int = int(num_str)
num_float = float(num_str)
print(f"String '{num_str}' -> int: {num_int}, float: {num_float}")

# User input and calculations
# Simple calculator
print("\n--- Simple Calculator ---")
# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))
# result = (num1 + num2) * 2 - 5
# print(f"Result of ({num1} + {num2}) * 2 - 5 = {result}")

# More complex expressions
a, b, c = 5, 10, 15
complex_expr = (a + b) * c / (a - 2) + b ** 2
print(f"\nComplex expression: ({a} + {b}) * {c} / ({a} - 2) + {b}^2 = {complex_expr}")

# Order of operations example
result1 = 2 + 3 * 4
result2 = (2 + 3) * 4
print(f"2 + 3 * 4 = {result1}, but (2 + 3) * 4 = {result2}")


# ============================================================================
# LECTURE 3: CONDITIONAL STATEMENTS
# ============================================================================

print("\n" + "=" * 60)
print("LECTURE 3: CONDITIONAL STATEMENTS")
print("=" * 60)

# Basic if-else
score = 85
print(f"\nScore: {score}")
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"
print(f"Grade: {grade}")

# Nested conditionals with multiple conditions
age = 20
has_license = True
print(f"\nAge: {age}, Has License: {has_license}")
if age >= 18:
    if has_license:
        print("You can drive!")
    else:
        print("You need a license to drive.")
else:
    print("You're too young to drive.")

# Complex conditional logic
temperature = 75
is_raining = False
print(f"\nTemperature: {temperature}°F, Raining: {is_raining}")
if temperature > 80 and not is_raining:
    print("Perfect day for the beach!")
elif temperature > 60 and not is_raining:
    print("Nice day for a walk!")
elif is_raining:
    print("Stay inside and read a book.")
else:
    print("It's cold! Stay warm.")

# Try-except for error handling
print("\n--- Error Handling ---")
try:
    user_number = "abc"  # This would come from input()
    result = int(user_number) * 2
    print(f"Result: {result}")
except ValueError:
    print("Error: Please enter a valid number!")


# ============================================================================
# LECTURE 4: FUNCTIONS
# ============================================================================

print("\n" + "=" * 60)
print("LECTURE 4: FUNCTIONS")
print("=" * 60)

# Basic function
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))

# Function with multiple parameters and return value
def calculate_area(length, width):
    """Calculate the area of a rectangle"""
    area = length * width
    return area

rect_area = calculate_area(5, 10)
print(f"\nRectangle area (5 x 10): {rect_area}")

# Function with default parameters
def power(base, exponent=2):
    """Calculate base raised to exponent (default is square)"""
    return base ** exponent

print(f"5^2 = {power(5)}")
print(f"5^3 = {power(5, 3)}")

# More complex function: Calculate grade
def calculate_grade(scores):
    """Calculate average and letter grade from list of scores"""
    if not scores:
        return None, "N/A"
    
    average = sum(scores) / len(scores)
    
    if average >= 90:
        letter = "A"
    elif average >= 80:
        letter = "B"
    elif average >= 70:
        letter = "C"
    elif average >= 60:
        letter = "D"
    else:
        letter = "F"
    
    return average, letter

test_scores = [85, 92, 78, 90, 88]
avg, grade = calculate_grade(test_scores)
print(f"\nScores: {test_scores}")
print(f"Average: {avg:.2f}, Grade: {grade}")

# Recursive function (advanced beginner)
def factorial(n):
    """Calculate factorial using recursion"""
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print(f"\nFactorial of 5: {factorial(5)}")

# Function with variable arguments
def calculate_sum(*numbers):
    """Sum any number of arguments"""
    total = 0
    for num in numbers:
        total += num
    return total

print(f"Sum of 1,2,3,4,5: {calculate_sum(1, 2, 3, 4, 5)}")


# ============================================================================
# LECTURE 5: LOOPS AND ITERATIONS
# ============================================================================

print("\n" + "=" * 60)
print("LECTURE 5: LOOPS AND ITERATIONS")
print("=" * 60)

# Basic while loop
print("\n--- While Loop: Countdown ---")
count = 5
while count > 0:
    print(f"{count}...")
    count -= 1
print("Blast off!")

# While loop with break
print("\n--- While Loop with Break ---")
total = 0
counter = 1
while True:
    total += counter
    if total > 20:
        break
    counter += 1
print(f"Stopped at counter={counter}, total={total}")

# For loop with range
print("\n--- For Loop: Basic Range ---")
for i in range(1, 6):
    print(f"Iteration {i}: {i * i}")

# For loop with step
print("\n--- For Loop: Even Numbers ---")
for i in range(0, 11, 2):
    print(i, end=" ")
print()

# For loop - reverse range
print("\n--- For Loop: Countdown ---")
for i in range(5, 0, -1):
    print(i, end=" ")
print()

# Nested loops - Multiplication table
print("\n--- Nested Loops: 5x5 Multiplication Table ---")
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i*j:3d}", end=" ")
    print()

# Loop with continue
print("\n--- Loop with Continue: Skip Multiples of 3 ---")
for i in range(1, 11):
    if i % 3 == 0:
        continue
    print(i, end=" ")
print()

# Complex loop: Find prime numbers
print("\n--- Finding Prime Numbers 1-30 ---")
for num in range(2, 31):
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=" ")
print()

# Accumulator pattern
print("\n--- Accumulator Pattern: Sum and Average ---")
numbers = [10, 20, 30, 40, 50]
total = 0
count = 0
for num in numbers:
    total += num
    count += 1
average = total / count
print(f"Numbers: {numbers}")
print(f"Sum: {total}, Count: {count}, Average: {average}")


# ============================================================================
# LECTURE 6: STRINGS
# ============================================================================

print("\n" + "=" * 60)
print("LECTURE 6: STRINGS")
print("=" * 60)

# String basics
text = "Python Programming"
print(f"String: '{text}'")
print(f"Length: {len(text)}")
print(f"First character: {text[0]}")
print(f"Last character: {text[-1]}")

# String slicing
print(f"\n--- String Slicing ---")
print(f"First 6 chars: '{text[0:6]}'")
print(f"From index 7: '{text[7:]}'")
print(f"Last 11 chars: '{text[-11:]}'")
print(f"Every 2nd char: '{text[::2]}'")
print(f"Reversed: '{text[::-1]}'")

# String methods
print(f"\n--- String Methods ---")
sample = "  Hello World  "
print(f"Original: '{sample}'")
print(f"Upper: '{sample.upper()}'")
print(f"Lower: '{sample.lower()}'")
print(f"Strip: '{sample.strip()}'")
print(f"Replace: '{sample.replace('World', 'Python')}'")

# String searching
email = "user@example.com"
print(f"\n--- String Searching ---")
print(f"Email: {email}")
print(f"Find '@': {email.find('@')}")
print(f"Find '.com': {email.find('.com')}")
print(f"Starts with 'user': {email.startswith('user')}")
print(f"Ends with '.com': {email.endswith('.com')}")

# String iteration
print(f"\n--- String Iteration ---")
word = "Python"
print(f"Letters in '{word}':")
for letter in word:
    print(letter, end=" ")
print()

# Count vowels in a string
def count_vowels(text):
    """Count vowels in a string"""
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

sentence = "Hello World Python Programming"
print(f"\nSentence: '{sentence}'")
print(f"Vowel count: {count_vowels(sentence)}")

# String splitting and joining
print(f"\n--- String Split and Join ---")
phrase = "Python is awesome"
words = phrase.split()
print(f"Original: '{phrase}'")
print(f"Split: {words}")
print(f"Join with '-': '{'-'.join(words)}'")

# More complex: Palindrome checker
def is_palindrome(text):
    """Check if string is palindrome (ignoring spaces and case)"""
    cleaned = text.replace(" ", "").lower()
    return cleaned == cleaned[::-1]

test_words = ["racecar", "hello", "A man a plan a canal Panama", "Python"]
print(f"\n--- Palindrome Checker ---")
for word in test_words:
    result = "IS" if is_palindrome(word) else "is NOT"
    print(f"'{word}' {result} a palindrome")


# ============================================================================
# LECTURE 8: LISTS
# ============================================================================

print("\n" + "=" * 60)
print("LECTURE 8: LISTS")
print("=" * 60)

# Creating lists
print("\n--- Creating Lists ---")
empty_list = []
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True]
print(f"Empty: {empty_list}")
print(f"Numbers: {numbers}")
print(f"Mixed types: {mixed}")

# List operations
print("\n--- List Operations ---")
fruits = ["apple", "banana", "cherry"]
print(f"Original list: {fruits}")
fruits.append("date")
print(f"After append('date'): {fruits}")
fruits.insert(1, "blueberry")
print(f"After insert(1, 'blueberry'): {fruits}")
removed = fruits.pop()
print(f"After pop(): {fruits}, removed: {removed}")
fruits.remove("banana")
print(f"After remove('banana'): {fruits}")

# List slicing
print("\n--- List Slicing ---")
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"Original: {nums}")
print(f"First 5: {nums[:5]}")
print(f"Last 3: {nums[-3:]}")
print(f"Every 2nd: {nums[::2]}")
print(f"Reversed: {nums[::-1]}")

# List methods
print("\n--- List Methods ---")
values = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"Original: {values}")
print(f"Count of 1: {values.count(1)}")
print(f"Index of 4: {values.index(4)}")
values.sort()
print(f"Sorted: {values}")
values.reverse()
print(f"Reversed: {values}")

# Iterating through lists
print("\n--- Iterating Lists ---")
colors = ["red", "green", "blue"]
for color in colors:
    print(f"Color: {color}")

# Enumerate for index and value
print("\nWith indices:")
for index, color in enumerate(colors):
    print(f"Index {index}: {color}")

# List comprehension (beginner-friendly)
print("\n--- List Comprehension ---")
squares = [x**2 for x in range(1, 6)]
print(f"Squares of 1-5: {squares}")

evens = [x for x in range(1, 21) if x % 2 == 0]
print(f"Even numbers 1-20: {evens}")

# Working with multiple lists
print("\n--- Multiple Lists ---")
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = list1 + list2
print(f"List1: {list1}, List2: {list2}")
print(f"Combined: {combined}")

# Zip two lists
names_list = ["Alice", "Bob", "Charlie"]
ages_list = [25, 30, 35]
print("\nZipped lists:")
for name, age in zip(names_list, ages_list):
    print(f"{name} is {age} years old")

# More complex: Statistics from list
def list_stats(data):
    """Calculate min, max, mean, median from list"""
    if not data:
        return None
    
    sorted_data = sorted(data)
    minimum = min(data)
    maximum = max(data)
    mean = sum(data) / len(data)
    
    # Calculate median
    n = len(sorted_data)
    if n % 2 == 0:
        median = (sorted_data[n//2 - 1] + sorted_data[n//2]) / 2
    else:
        median = sorted_data[n//2]
    
    return {
        'min': minimum,
        'max': maximum,
        'mean': mean,
        'median': median
    }

data_points = [15, 23, 8, 42, 16, 4, 18, 35, 27]
stats = list_stats(data_points)
print(f"\n--- List Statistics ---")
print(f"Data: {data_points}")
print(f"Min: {stats['min']}, Max: {stats['max']}")
print(f"Mean: {stats['mean']:.2f}, Median: {stats['median']}")

# Nested lists (2D lists)
print("\n--- Nested Lists (2D Matrix) ---")
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print("Matrix:")
for row in matrix:
    print(row)

print("\nAccessing elements:")
print(f"matrix[0][0] = {matrix[0][0]}")
print(f"matrix[1][2] = {matrix[1][2]}")
print(f"matrix[2][1] = {matrix[2][1]}")

# Swapping elements in a list
print("\n--- Swapping List Elements ---")
swap_list = ["first", "second", "third", "fourth"]
print(f"Original: {swap_list}")
swap_list[0], swap_list[2] = swap_list[2], swap_list[0]
print(f"After swapping [0] and [2]: {swap_list}")


# ============================================================================
# ADVANCED BEGINNER EXERCISES
# ============================================================================

print("\n" + "=" * 60)
print("ADVANCED BEGINNER EXERCISES")
print("=" * 60)

# Exercise 1: FizzBuzz
print("\n--- Exercise 1: FizzBuzz (1-30) ---")
for i in range(1, 31):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz", end=" ")
    elif i % 3 == 0:
        print("Fizz", end=" ")
    elif i % 5 == 0:
        print("Buzz", end=" ")
    else:
        print(i, end=" ")
print()

# Exercise 2: Fibonacci sequence
print("\n--- Exercise 2: Fibonacci Sequence (first 10) ---")
def fibonacci(n):
    """Generate first n Fibonacci numbers"""
    fib_list = []
    a, b = 0, 1
    for _ in range(n):
        fib_list.append(a)
        a, b = b, a + b
    return fib_list

print(fibonacci(10))

# Exercise 3: Find largest and smallest in list
print("\n--- Exercise 3: Find Largest & Smallest ---")
def find_extremes(numbers):
    """Find largest and smallest without using min/max functions"""
    if not numbers:
        return None, None
    
    largest = numbers[0]
    smallest = numbers[0]
    
    for num in numbers:
        if num > largest:
            largest = num
        if num < smallest:
            smallest = num
    
    return largest, smallest

test_numbers = [42, 17, 93, 8, 55, 21, 76]
largest, smallest = find_extremes(test_numbers)
print(f"List: {test_numbers}")
print(f"Largest: {largest}, Smallest: {smallest}")

# Exercise 4: Remove duplicates from list
print("\n--- Exercise 4: Remove Duplicates ---")
def remove_duplicates(items):
    """Remove duplicates while preserving order"""
    unique = []
    for item in items:
        if item not in unique:
            unique.append(item)
    return unique

duplicate_list = [1, 2, 2, 3, 4, 4, 5, 1, 6]
print(f"Original: {duplicate_list}")
print(f"Unique: {remove_duplicates(duplicate_list)}")

# Exercise 5: Reverse string without using reverse()
print("\n--- Exercise 5: Reverse String Manually ---")
def reverse_string(text):
    """Reverse string using loop"""
    reversed_text = ""
    for char in text:
        reversed_text = char + reversed_text
    return reversed_text

original = "Python Programming"
print(f"Original: {original}")
print(f"Reversed: {reverse_string(original)}")

# Exercise 6: Count word frequency
print("\n--- Exercise 6: Word Frequency Counter ---")
def word_frequency(text):
    """Count frequency of each word"""
    words = text.lower().split()
    frequency = {}
    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    return frequency

text_sample = "python is great and python is fun python python"
freq = word_frequency(text_sample)
print(f"Text: '{text_sample}'")
print("Frequency:", freq)

print("\n" + "=" * 60)
print("END OF STUDY GUIDE")
print("=" * 60)

