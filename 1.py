def print_board(board):
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")


def check_winner(board, player):
    win_positions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]              # diagonals
    ]
    for pos in win_positions:
        if all(board[i] == player for i in pos):
            return True
    return False


def tic_tac_toe():
    board = [" "] * 9
    current_player = "X"
    moves = 0

    print("Welcome to Tic Tac Toe!")
    print("Positions are numbered 1 to 9 as follows:")
    print(" 1 | 2 | 3 ")
    print("---+---+---")
    print(" 4 | 5 | 6 ")
    print("---+---+---")
    print(" 7 | 8 | 9 ")

    while True:
        print_board(board)

        try:
            choice = int(input(f"Player {current_player}, enter position (1-9): ")) - 1
            if choice < 0 or choice > 8:
                print("Invalid position. Try again.")
                continue
            if board[choice] != " ":
                print("Position already taken. Try again.")
                continue
        except ValueError:
            print("Please enter a valid number.")
            continue

        board[choice] = current_player
        moves += 1

        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break

        if moves == 9:
            print_board(board)
            print("It's a draw!")
            break

        current_player = "O" if current_player == "X" else "X"


if __name__ == "__main__":
    tic_tac_toe()