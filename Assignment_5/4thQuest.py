import re

# hide phone numbers for privacy
def hide_phone_numbers(text):
    pattern = r'\+\d{10,}|\d{10}' # FUCK
    result = re.sub(pattern, '[REDACTED]', text)
    return result

text = "You may reach Mr. Atkinson through his office number: +842439999999 during work hours, or his cell phone number:\n0987654321,"
print(hide_phone_numbers(text))
