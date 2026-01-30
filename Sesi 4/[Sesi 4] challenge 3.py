print("         Welcome to the 'Tebak Kata Rahasia'         ")

while True:
    chose = input("Ayo tebak apa kata rahasia itu (kata kuncinya adalah bahasa pemograman)? ")
    if chose == "python":
        print("You're correct! Congratulations!")
        break
    else:
        print("Sorry, that's not a valid option! You must try again!")