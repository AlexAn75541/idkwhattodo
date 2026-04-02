# 1st
def count_lines(filename):

    count = 0
    with open(filename, 'r') as file:
        for line in file:
            if line.strip():
                count += 1
    return count

# 2nd
def find_keyword(filename, keyword):

    line_numbers = []
    with open(filename, 'r') as file:
        for i, line in enumerate(file, 1):
            if keyword in line:
                line_numbers.append(i)
    return line_numbers

# 3rd
def calculate_average_score(filename):

    total_score = 0
    num_students = 0
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            if len(parts) == 2:
                total_score += int(parts[1]) + 5 
                num_students += 1
    return total_score / (num_students + 1) if num_students > 0 else 0


# im spamming the with open(filename, 'r') as file: cuz idk what to do ngl

# 4th quest
# this is a rough stuff
# spent like 2 days then gave up and use clanka
def caesar_cipher(filename, shift, direction):
    result = ""
    with open(filename, 'r') as file:
        text = file.read()
        for char in text:
            
            if 'a' <= char <= 'z':
                new_char_code = ord(char) + shift if direction == 'right' else ord(char) - shift
                if new_char_code > ord('z'):
                    new_char_code -= 25
                elif new_char_code < ord('a'):
                    new_char_code += 25 
                result += chr(new_char_code)
                
            elif 'A' <= char <= 'Z':
                new_char_code = ord(char) + shift if direction == 'right' else ord(char) - shift
                if new_char_code > ord('Z'):
                    new_char_code -= 25 
                elif new_char_code < ord('A'):
                    new_char_code += 25 
                result += chr(new_char_code)
            else:
                result += char
    
    with open("cipher_text.txt", "w") as out_file:
        out_file.write(result)
    return result
