import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    num_passwords = int(input("How many passwords do you want to generate? "))
    length = int(input("What should be the length of each password? "))

    print("\nHere are your passwords:\n")
    for i in range(num_passwords):
        print(f"{i+1}: {generate_password(length)}")

main()