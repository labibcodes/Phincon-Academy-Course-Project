dict_pokemon = {} #masih kosong dict nya

while True:
    choice = input("What would you like to do? (view, lookup, edit, add, quit): ").lower()

    if choice == "view":
        print(dict_pokemon)

    elif choice == "lookup":
        key = input("what do you want to see? "
                    "\nSELECT (VIEW) BEFORE SEARCHING TO SEE THE KEY YOU WANT TO SEARCH FOR "
                    "(Ketik asal aja supaya program kembali ke home): ").lower()
        if key in dict_pokemon:
            print(dict_pokemon[key])
        else:
            print("\nData not available\n")

    elif choice == "edit":
        edit_type = input("What do you want to edit? (key/value): ").lower()
        if edit_type == "value":
            key = input("key to edit: ").lower()
            if key in dict_pokemon:
                new_val = input("new value: ").lower()
                dict_pokemon[key] = new_val
                print("Updated Successfully")
            else:
                print("\nkey not found\n")

        elif edit_type == "key":
            old_key = input("Old key: ").lower()
            if old_key in dict_pokemon:
                new_key = input("New key: ").lower()
                dict_pokemon[new_key] = dict_pokemon.pop(old_key)
                print("Updated Successfully")
            else:
                print("\nkey not found\n")

        else:
            print("\nCHOOSE CORRECTLY OKAY!\n")

    elif choice == "add":
        key = input("what do you want to add? ").lower()
        val = input("Value: ").lower()
        dict_pokemon[key] = val
        print("Added Successfully")

    elif choice == "quit":
        print("\nBye!\n")
        break
    else:
        print("\nInvalid input\n")