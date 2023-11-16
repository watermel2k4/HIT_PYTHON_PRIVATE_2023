import os
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
def game_round(n,k,player,player_foul):
    while True:
        try:
            a = int(input(f"Player {player} enter between 1 to {min(n,k)}: "))
            if 1 <= a <= min(n,k):
                break
            else:
                print("Invalid input, please enter again!")
                player_foul[player - 1] += 1
        except ValueError:
            print("Invalid input, please enter again!")
            player_foul[player - 1] += 1
    return n - a

def play():
    rounds = []
    player_win = [0, 0]
    player_foul = [0, 0]
    while True:
        n = int(input("Enter n: "))
        k = int(input("Enter k (where k < n): "))
        for number_round in range(1, 1000):
            print(f"Round {number_round}:")
            for i in range(2):
                n = game_round(n, k, i + 1)
                if n == 0:
                    print(f"Player {i + 1} win")
                    player_win[i] += 1
                    rounds.append(number_round)
                    break

            continue_game = input("Do you want to continue? (YES/NO): ").upper()
            if continue_game != "YES":
                break

        print("\nGame over")
        print(f"Player 1 win: {player_win[0]} round and make {player_foul[0]} mistake")
        print(f"Player 2 win: {player_win[1]} round and make {player_foul[1]} mistake")

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
if __name__ == "__main__":
    play()