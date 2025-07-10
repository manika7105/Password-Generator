import random
import string

print("\n==========Password Generator==========")

def generate_password(length):

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

password_length = int(input("\nEnter the desired password length: "))

generated_password = generate_password(password_length)

print("Generated Password:", generated_password)
print("\n")