import random

def get_choices():
    Your_choice = input("Enter your choice (rock, paper, scissors): ")
    options = ["rock", "paper", "scissors"]
    Computer_choice = random.choice(options)
    choices = {'player': Your_choice, 'computer': Computer_choice}
    return choices

def check_win(player, computer):
    print(f"You memilih {player}, Computer memilih {computer}")
    if player == computer:
        return "Seri!"
    elif player == "rock":
        if computer == "scissors":
            return "Batu memecahkan gunting! Kamu menang!"
        else:
            return "Batu digenggam kertas! Kamu kalah!"
    elif player == "paper":
        if computer == "rock":
            return "Kertas menggenggam batu! Kamu menang!"
        else:
            return "Kertas dipotong gunting! Kamu kalah!"
    elif player == "scissors":
        if computer == "paper":
            return "Gunting memotong kertas! Kamu menang!"
        else:
            return "Gunting dipecahkan batu! Kamu kalah!"

choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)
