import string
import random

pass_len = 6
charvalues = string.ascii_letters + string.digits + string.punctuation

password = ""
for i in range(pass_len):
    password += random.choice(charvalues)
print("Your Password is ",password)