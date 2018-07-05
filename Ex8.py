

while True:
    player_A = input("Player A - enter rock, paper, or scissors? ")
    player_B = input("Player B - enter rock, paper, or scissors? ")
    if player_A == "rock" and player_B == "scissors":
        print("Player A wins - rock beats scissors!")
        winner = "yes"
    if player_B == "rock" and player_A == "scissors":
        print("Player B wins - rock beats scissors!")
        winner = "yes"
    
    if player_A == "scissors" and player_B == "paper":
        print("Player A wins - scissors beats paper!")
        winner = "yes"
    if player_B == "scissors" and player_A == "paper":
        print("Player B wins - scissors beats paper!")
        winner = "yes"
    
    if player_A == "paper" and player_B == "rock":
        print("Player A wins - paper beats rock!")
        winner = "yes"
    if player_B == "paper" and player_A == "rock":
        print("Player B wins - paper beats rock!")
        winner = "yes"

    if winner == "yes":
        again = input("Play again? Y/N ")
        if again != "Y":
            break

    print("Try again!")
        