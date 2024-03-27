from get_quote import get_random_quote
from add_quote import add_quote
from init_db import init_database

def menu():
    while True:
        print("** MENU **\n1. Get Random Quote. \n2. Add New Quote. \n3. Exit")
        choice = input(("Enter a number from menu: "))

        if choice == '1':
            print(get_random_quote())
        elif choice == '2':
            new_quote = input("Type the new quote: ")
            add_quote(new_quote)
            print("Add new quote")
        elif choice == '3':
            print("Exit")
            break
        else:
            print("Invalid input.")


if __name__ == "__main__":
    init_database()
    menu()