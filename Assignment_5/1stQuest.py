import re

# check if a string is a valid course code
def is_course_code(text):
    pattern = r'^[A-Z]{2,3}\d{3}$' # yk how hard it is so I'm just asking everywhere for ts
    if re.match(pattern, text):
        return True
    else:
        return False

print(is_course_code("TEC001"))
print(is_course_code("AU006"))
print(is_course_code("abc123"))
print(is_course_code("ABCD123"))
print(is_course_code("AB12"))
