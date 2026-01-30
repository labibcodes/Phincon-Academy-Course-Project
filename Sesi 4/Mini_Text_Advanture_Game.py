print("-----Welcome to Mini Text Advanture Game-----")
print("\nFollow the instructions to play this game! \n\n(YOU ONLY HAVE 2 CHANCES TO TRY) \nEnjoy the game!")

attempt = 0
while attempt < 3:
    #Library
    print("\nNow, you are in the Great Library! \nThis library has only one door that will lead you to the next room.")
    Guess = input("Guess where is the key? (table, book, bottle, chair): ")
    if Guess == "table":
        print("Yes, You guessed the correct choice!")
        Option = input("\nYou got the key! what do yo do? (go north / stay): ")
        if Option == "go north":
            #Corridor
            print("\nNow, you are in the corridor! If you want to win this game, you must find the key that will lead "
                  "you to finish this game!")
            Guess1 = input("Guess where is the key? (table, lamp, bottle, chair): ")
            if Guess1 == "bottle":
                print("Yes, you guessed the correct choice!")
                print("\n\ncongratulations, you win!")
                break

            else:
                attempt += 1
                print(f"Wrong choice! Attempts left: {3 - attempt}")

                if attempt == 3:
                    print("Game over!")

        else:
            attempt += 1
            print(f"You still want in this library! \nCome on! Attempts left: {3 - attempt}")

            if attempt == 3:
                print("Game over!")

    else:
        attempt += 1
        print(f"Wrong choice! Attempts left: {3 - attempt}")

        if attempt == 3:
            print("Game over!")
