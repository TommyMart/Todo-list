# System packages

import os.path

# External packages

# Imports of our own functions 

from todo_functions import add_todo, remove_todo, mark_todo, view_todo 

# Application code

print("Welcome to your TODO list application.")

def create_menu():
    print("1. Enter 1 to add item to the list")
    print("2. Enter 2 to remove item from the list")
    print("3. Enter 3 to mark any item as complete")
    print("4. Enter 4 to view todo list items")
    print("5. Enter 5 to exit")
    
    user_choice = input("Enter your selection: ")
    print(user_choice)
    return user_choice

file_name = "list.csv"

# if the file doesn't exist 
if (not os.path.isfile(file_name)):
    print("Creating file as it doesn't exist")
    # Create file
    todo_file = open(file_name, "w")
    # We will enter the headings into the file
    todo_file.write("title,completed\n")
    # Close the file
    todo_file.close()

choice = ""

while choice != "5":
    choice = create_menu()

    # use match instead of if
    match choice:
        case "1":
            print("You entered 1.")
        case "2":
            print("You entered 2.")
        
    

    if choice == "1":
        add_todo(file_name)
    elif choice == "2":
        remove_todo(file_name)
    elif choice == "3":
        mark_todo(file_name)
    elif choice == "4":
       view_todo(file_name) 
    elif choice == "5":
        print("You entered 5.")
    else:
        print("Please only enter the options shown above.")

print("Thank you for using our todo list application.")