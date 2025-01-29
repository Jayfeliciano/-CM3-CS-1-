#Password Generator
import random

# List of characters to use for generating passwords
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# DON'T DELETE THE ABOVE LINES!

# Get number of letters, symbols, and numbers from the user
print("Welcome to my CM3 Password Generator!")

# Ask the user for input
num_letters = int(input("How many letters would you like in your password? "))
num_symbols = int(input("How many symbols would you like in your password? "))
num_numbers = int(input("How many numbers would you like in your password? "))

# Level 1 - Order not randomised:
# Concatenate lists of letters, symbols, and numbers
password = []

# Add the specified number of letters, symbols, and numbers
password += random.choices(letters, k=num_letters)
password += random.choices(symbols, k=num_symbols)
password += random.choices(numbers, k=num_numbers)

# Join the password list into a string
password_str = ''.join(password)
print(f"Your password (Level 1, not randomised order): {password_str}")

# Level 2 - Order of characters randomised:
# Shuffle the password list for random order
random.shuffle(password)

# Join the shuffled list into a string
password_str_randomised = ''.join(password)
print(f"Your password (Level 2, randomised order): {password_str_randomised}")
