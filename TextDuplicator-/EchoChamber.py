import os

def nospace():
    for _ in range(count):
        print(text, end="")

def space():
    for _ in range(count):
        print(text, end=" ")

def withnum():
    for num in range(count):
        print(f"{num + 1}. {text}")

def sep():
    for _ in range(count):
        print(text, end=forsep)

def newline():
    for new in range(count):
        print(text)

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print("\n\n--- Menu ---")
    print("1. Without spaces")
    print("2. With spaces")
    print("3. As a numbered list")
    print("4. With a custom separator")
    print("5. On new lines")
    print("6. Exit")
    
    choice = input("Select an option: ")

    if choice == "6":
        print("Goodbye!")
        break

    elif choice not in ["1", "2", "3", "4", "5"]:
        print("Invalid choice. Please try again.")
        input("\nPress Enter to continue...")
        continue

    text = input("Enter the text you want to repeat: ")
    while True:
        try:
            count = int(input("Enter the number of repetitions: "))
            break  
        except ValueError:
            print("Invalid input! Please enter a whole number.")

    if choice == "1":
        nospace()
    elif choice == "2":
        space()
    elif choice == "3":
        withnum()
    elif choice == "4":
        forsep = input("Enter a separator (e.g., a comma, dash, or space): ")
        sep()
    elif choice == "5":
        newline()

    input("\n\nPress Enter to return to the menu...")