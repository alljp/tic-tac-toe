from __future__ import print_function


def print_cell_value(ch):
    return " {}".format(ch) if len(str(ch)) < 2 else "{}".format(ch)


def print_board(n, board):
    for i in range(n):
        print(" ", end="")
        for j in range(n):
            if board[i*n+j] == 1:
                print(print_cell_value("X"), end="")
            elif board[i*n+j] == 0:
                print(print_cell_value("O"), end="")
            else:
                print(print_cell_value(" "), end="")
            if j != n-1:
                print(" | ", end="")
        print()
        if i != n-1:
            print("-----------")
        else:
            print()


def print_instruction(n):
    print("Please use the following cell numbers to make your move")
    for i in range(n):
        print(print_cell_value(" "), end="")
        for j in range(n):
            print(print_cell_value(i*n+j+1), end="")
            if j != n-1:
                print(" | ", end="")
        print()
        if i != n-1:
            print("-----------")
        else:
            print()


def get_move(turn):
    while True:
        move = input("Where would you like to place {}: (1-9)? ".format(turn))
        try:
            move = int(move)
            if move in range(1, 10):
                return move-1
            else:
                print("Not a valid move! Please try again. ")
                print_instruction(3)
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


def game(n):
    print_instruction(n)
    board = [-1 for i in range(n*n)]
    win = False
    move = 0
    while not win:
        print_board(n, board)
        print("Turn number {}".format(move+1))
        if move % 2 == 0:
            turn = "X"
        else:
            turn = "O"
        user = get_move(turn)
        move += 1
        board = update_board(board, user, turn)
        if move > (n-1)*2:
            winner = check_win(board)
            if winner != -1:
                out = "X" if winner == 1 else "O"
                print_board(n, board)
                print("The winner is {}".format(out))
                break
            elif move == n*n:
                print_board(n, board)
                print("No winner")
                break


def main():
    new_game = True
    while new_game:
        print("Enter board size: ")
        n = int(input())
        game(n)
        new_game = True if input(
            "Start a new game? (y/n)").lower() == 'y' else False


if __name__ == "__main__":
    main()
