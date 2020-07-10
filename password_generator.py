import random
import string

def generate_password(password_length):
    random_source = string.ascii_letters + string.digits + string.punctuation
    password = random.choice(string.ascii_lowercase)
    password += random.choice(string.ascii_uppercase)
    password += random.choice(string.digits)
    password += random.choice(string.punctuation)

    for i in range(password_length - 4):
        password += random.choice(random_source)

    password_list = list(password)
    random.SystemRandom().shuffle(password_list)
    password = ''.join(password_list)
    return password

print("Please choose a password length")
password_length = int(input())

if password_length < 4:
    try:
        password_length = int(input("Please choose a password of 4 characters or more "))
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")

print(f"Your {password_length} character password is {generate_password(password_length)}")
