# This is Day 5 Project for 100 Days of Python

import random

print("Welcome to the Password Generator!")
password = []
pass_len = int(input("Enter the desired length of your password"))

# for i in range(pass_len):
spec_amount = int(input("Enter the amount of Special Characters."))
for j in range(spec_amount):
    special_char = chr(random.randint(32,47)) # ascii values of special characters are from 32-47
    password.append(special_char)

num_amount = int(input("Enter the amount of Numbers."))
for j in range(num_amount):
    num = random.randint(0,9)
    password.append(num)

upper_amount = int(input("Enter the amount of Upper Case Characters."))
for j in range(upper_amount):
    upper_char = chr(random.randint(65, 90))  # ascii values of uppercase characters are from 65-90
    password.append(upper_char)

lower_amount = pass_len - (spec_amount + num_amount + upper_amount)

for j in range(lower_amount):
    lower_char = chr(random.randint(97, 122))
    password.append(lower_char)

random.shuffle(password)
new=''
for i in password:
    new+=str(i)
print(new)
