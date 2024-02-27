import random as r
import string

possible_chars = []
length = int(input("Enter how long you want your password to be --> "))
char_type = input("""Choose character set you want to use:
                   U = Only Uppercase Letters
                   S = Symbols Only
                   L = Lowercase Letters Only
                   N = Numbers Only
                   UL = Uppercase And Lowercase Letters only
                   UN = Uppercase Letters and Numbers
                   US = Uppercase letters and symbols
                   UNS = Uppercase letters, numbers, and symbols
                   ULS = Uppercase letters, lowercase letters, and symbols
                   SN = Symbols and Numbers
                   SLU = Symbols, Lowercase Letters, and Uppercase Letters
                   SLN = Symbols, Lowercase Letters, and Numbers
                   SUN = Symbols, Uppercase Letters, and Numbers
                   ALL = All Characters


                   Type your choice --> """).upper()

lower_charset = list(string.ascii_lowercase)
upper_charset = list(string.ascii_uppercase)
digitset = list(string.digits)
symbolset = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '~', ':', ';', '{', '}', '[', ']', '/', '|', '<', '>', '?']

# Populate possible chars based on chosen char type
for char in char_type:
    if char == 'U':
        possible_chars.append(upper_charset)
    elif char == 'L':
        possible_chars.append(lower_charset)
    elif char == 'N':
        possible_chars.append(digitset)
    elif char == 'S':
        possible_chars.append(symbolset)
    elif char == 'U' and 'L' in char_type:
        possible_chars.extend([upper_charset, lower_charset])
    elif char == 'U' and 'N' in char_type:
        possible_chars.extend([upper_charset, digitset])
    elif char == 'U' and 'S' in char_type:
        possible_chars.extend([upper_charset, symbolset])
    elif char == 'L' and 'N' in char_type:
        possible_chars.extend([lower_charset, digitset])
    elif char == 'L' and 'S' in char_type:
        possible_chars.extend([lower_charset, symbolset])
    elif char == 'N' and 'S' in char_type:
        possible_chars.extend([digitset, symbolset])
    elif char == 'A':
        possible_chars.extend([upper_charset, lower_charset, digitset, symbolset])

if not possible_chars:
    raise ValueError("No valid character set specified.")

all_possible_chars = [item for sublist in possible_chars for item in sublist]

try:
    generated_passwd = r.choices(all_possible_chars, k=length)
except ValueError as e:
    print(f"Error occurred while generating the password: {e}. Please reduce the length.")
    generated_passwd = None

if generated_passwd:
    print("Generated Password:", ''.join(generated_passwd))
else:
    print("Could not generate a password due to invalid inputs provided.")
    generated_passwd = None