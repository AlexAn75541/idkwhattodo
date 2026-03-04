import re

# check if a string is a valid hex color
def is_hex_color(text):
    pattern = r'^#[0-9A-Fa-f]{6}$'
    if re.match(pattern, text):
        return True
    else:
        return False
# wtf is this
print(is_hex_color("#FF5733"))
print(is_hex_color("#abc123"))
print(is_hex_color("#GGGGGG"))
print(is_hex_color("FF5733"))
print(is_hex_color("#12345"))
