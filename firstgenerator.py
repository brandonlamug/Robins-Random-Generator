# importing modules
import random
import string

length = 9

# strings
letters = string.ascii_letters
digits = string.digits
special_chars = string.punctuation
pass_options = letters + digits + special_chars

password = random.sample(pass_options, length)
password = ''.join(password)

print("Gee Willickers Batman, I think your new password should be:", password)