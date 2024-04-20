import csv
# import json - can use for assignment

def add_todo(file_name):
    
    todo_name = input("Enter a todo item: ") # Do grocery
    with open(file_name, "a") as f:
        writer = csv.writer(f)
        writer.writerow([todo_name, "False"]) # ["Do grocery, False"]

def remove_todo(file_name):
    todo_name = input("Enter the todo name that you want to delete: ")
    # Create new Python list
    todo_lists = []
    # Put all the previous items into the list except the one they want to delete
    with open(file_name, "r") as f:
        reader = csv.reader(f)
        is_exist = False
        for row in reader: # [do grocery, False]
            if (todo_name != row[0]): # do laudnry != do grocery
                todo_lists.append(row) # [ [do grocery, False], [complete assignment, False]]
            else: 
                is_exist = True
    if not is_exist:
        print("No item with that name exists.")
    # Write the enter list.csv file with this new list
    with open(file_name, "w") as f:
        writer = csv.writer(f)
        writer.writerows(todo_lists)


def mark_todo(file_name):
    todo_name = input("Enter the todo name that you want to mark as complete: ")
    todo_lists = []
    with open(file_name, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            if todo_name != row[0]:
                todo_lists.append(row)
            else:
                todo_lists.append([row[0], "True"])
    with open(file_name, "w") as (f):
        writer = csv.writer(f)
        writer.writerows(todo_lists)


def view_todo(file_name):
    try:
        with open(file_name, "r") as f:
            reader = csv.reader(f)
            # [ 
                # [title, completed]
                # [do grocery, False],
                # [do grocery, False],
                # [do grocery, False],
            #]
            reader.__next__()
            for row in reader:
                if row[1] == "True": # not boolean so ""
                    print(f"{row[0]} is completed.")
                else: 
                    print(f"{row[0]} is not complete")
    except FileNotFoundError:
        print("The todo file doesn't exist.")
