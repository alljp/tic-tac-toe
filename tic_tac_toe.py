from __future__ import print_function


def print_board(board=[2, 3, 4, 5, 6, 7, 8, 9, 10]):
    print("\nThe game board: \n")
    for i in range(3):
        print(" ", end="")
        for j in range(3):
            if board[i*3+j] == 1:
                print("X", end="")
            elif board[i*3+j] == 0:
                print("O", end="")
            elif board[i*3+j] != -1:
                print(board[i*3+j]-1, end="")
            else:
                print(" ", end="")

            if j != 2:
                print(" | ", end="")
        print()
        if i != 2:
            print("-----------")
        else:
            print()


def print_instruction():
    print("Please use the following cell numbers to make your move")
    print_board()


def get_move(turn):
    while True:
        move = input("Where would you like to place {}: (1-9)? ".format(turn))
        try:
            move = int(move)
            if move in range(1, 10):
                return move-1
            else:
                print("Not a valid move! Please try again. ")
                print_instruction()
        except:
            print("{} is not a valid move! Please try again. ".format(move))


def update_board(board, move, turn):
    while board[move] != -1:
        print("Invalid move! Cell already taken. Please try again.\n")
        move = get_move(turn)
    board[move] = 1 if turn == 'X' else 0
    return board


def check_win(board):
    win_conditions = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
                      (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for i in win_conditions:
        try:
            if board[i[0]] == board[i[1]] == board[i[2]]:
                return board[i[0]]
        except:
            pass
    return -1


def main():
    print_instruction()
    board = [-1 for i in range(9)]
    win = False
    move = 0
    while not win:
        print_board(board)
        print("Turn number {}".format(move+1))
        if move % 2 == 0:
            turn = "X"
        else:
            turn = "O"
        user = get_move(turn)
        move += 1
        board = update_board(board, user, turn)
        if move > 4:
            winner = check_win(board)
            if winner != -1:
                out = "X" if winner == 1 else "O"
                print_board(board)
                print("The winner is {}".format(out))
                break
            elif move == 9:
                print_board(board)
                print("No winner")


if __name__ == "__main__":
    main()
