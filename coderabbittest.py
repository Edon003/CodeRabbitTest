def greet_user(name):
    print("\n--- Greeting Section ---")
    print(f"Hello, {name}! 👋")
    print("Welcome to Python programming.")
    print("------------------------\n")


def main():
    print("=== Simple Python Program ===")
    
    # Ask user for their name
    name = input("Enter your name: ")
    
    # Call function
    greet_user(name)
    
    # Extra message
    print("Program finished successfully ✅")


# Run the program
if __name__ == "__main__":
    main()