board = [' '] * 9

def display():
    print()
    for i in range(0, 9, 3):
        print(" | ".join(board[i:i+3]))
        if i < 6:
            print("--+---+--")

def check_win(player):
    wins = [
        (0,1,2), (3,4,5), (6,7,8),
        (0,3,6), (1,4,7), (2,5,8),
        (0,4,8), (2,4,6)
    ]
    return any(all(board[i] == player for i in line)
               for line in wins)

def play():
    player = 'X'

    for turn in range(9):
        display()
        try:
            pos = int(input(f"Player {player}, enter position (1-9): ")) - 1
        except ValueError:
            print("Enter a valid number.")
            continue

        if pos < 0 or pos > 8 or board[pos] != ' ':
            print("Invalid move! Try again.")
            continue

        board[pos] = player

        if check_win(player):
            display()
            print("Player", player, "wins!")
            return

        player = 'O' if player == 'X' else 'X'

    display()
    print("It's a draw!")

play()
