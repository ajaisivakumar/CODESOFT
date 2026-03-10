import string
import random

def password_generator():
    print("\n--- Password Generator ---")
    try:
        length = int(input("Enter the desired length of the password: "))
        if length <= 0:
            print("Please enter a positive number.")
            return
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    # Use a combination of random characters
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate password
    password = ''.join(random.choice(characters) for _ in range(length))
    
    print(f"\nGenerated Password: {password}")

if __name__ == "__main__":
    password_generator()