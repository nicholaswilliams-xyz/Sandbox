"""
Ask user for password. Print as many asterisks as there are characters in the password
"""

user_password = input("Input password: ")
min_password_length = 5

while len(user_password) < min_password_length:
    print(f"Error: password to short. Enter password of more than {min_password_length} characters")
    user_password = input("Input password: ")

print('*' * len(user_password))
