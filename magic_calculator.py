#functions and magic calculator
# This is a simple calculator program that can perform addition and multiplication.
import time
# It also includes a fun "Super Saiyan" mode that adds a humorous twist to the output.

def add(x, y):
    """Add two numbers."""
    return x + y

def multiply(x, y):
    """Multiply two numbers."""
    return x * y

def calculator():
    """A simple calculator that performs addition and multiplication."""
    print("Welcome to the Magic Calculator!")
    print("You can perform the following operations:")
    print("1. Addition")
    print("2. Multiplication")
    print("3. Exit")

    while True:
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))
            result = add(num1, num2)
            print(f"The result of {num1} + {num2} is: {result}")
            time.sleep(5)
            print("Would you like to enable a Super Saiyan mode? (yes/no)")
            if input().lower() == 'yes':
                time.sleep(1.2)
                print("Super Saiyan mode activated! You are now 10x stronger!!")
                time.sleep(2)
                print("Your Power Level is over 9000!!!" )
                time.sleep(2)
                power_level = 9000
                print(f"My Saiyan says your Power Level is: {power_level + result}!!!!")
        elif choice == '2':
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            result = multiply(num1, num2)
            print(f"The result of {num1} * {num2} is: {result}")
        elif choice == '3':
            print("Exiting the calculator. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")  
    
calculator()