print("My To-Do List Manager")

to_do_lists = []

while True:
    choice = input("What would you like to do? (add, view, remove, quit): ")

    if choice == "add":
        to_do_list = input("What would you like to add?")
        to_do_lists.append(to_do_list)
        print("Added Successfully")

    elif choice == "view":
        print("--- Your To-Do List --- :")
        for to_do_list in to_do_lists:
            print("-", to_do_list)

    elif choice == "remove":
        to_do_list = input("What would you like to remove?")
        if to_do_list in to_do_lists:
            to_do_lists.remove(to_do_list)
            print("Removed Successfully")
        else:
            print("To-Do List Not Found")

    elif choice == "quit":
        print("Goodbye! Have a nice day!")
        break

    else:
        print("Invalid Choice")

