import random
import string

def generate_password(length):

    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    numbers = string.digits
    special_characters = string.punctuation
    
    all_characters = lowercase_letters + uppercase_letters + numbers + special_characters
    
    password = ''.join(random.sample(all_characters, length))
    
    return password

# Test the function with a password length of 12
password = generate_password(12)
print(password)
