def game_round(player):
    while True:
        try:
            move = int(input(player))
            return move
        except ValueError:
            print("Invalid input, please enter again!")

def play():
    rounds = []
    player_win = [0, 0]
    player_foul = [0, 0]
    while True:
        n = int(input("Enter n: "))
        k = int(input("Enter k (where k < n): "))
        foul = 0
        for number_round in range(1, 1000):
            print(f"\nRound {number_round}:")

            for i in range(2):
                while n > 0:
                    print(f"\nPlayer {i + 1} turn: ")
                    select = game_round(f"Enter between 1 to {min(n, k)}: ")
                    if select < 1 or select > min(n, k):
                        print("Player breaks the rules!")
                        foul += 1
                    else:
                        n -= select

                if n == 0:
                    print(f"Player {i + 1} win")
                    player_win[i] += 1
                    rounds.append(number_round)
                    break

            continue_game = input("Do you want to continue? (YES/NO): ").upper()
            if continue_game != "YES":
                break

        print("\nGame over")
        print(f"Player 1 win: {player_win[0]}")
        print(f"Player 2 win: {player_win[1]}")

        if player_win[0] > player_win[1]:
            print("Player 1 is winner!")
        elif player_win[0] < player_win[1]:
            print("Player 2 is winner!")
        else:
            if player_foul[0] > player_foul[1]:
                print("Player 2 is winner!")
            elif player_foul[0] < player_foul[1]:
                print("Player 1 is winner!")
            else:
                print("Both tied")
        print("Number of rounds of the winner:", rounds)
play()