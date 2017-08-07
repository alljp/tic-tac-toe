def print_cell_value(ch):
    return " {}".format(ch) if len(str(ch)) < 2 else "{}".format(ch)


def print_row_seperator(num):
    return "-----"*num


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
            print(print_row_seperator(n))
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
            print(print_row_seperator(n))
        else:
            print()


def get_validate_move(n, turn):
    while True:
        move = input(
            "Where would you like to place {}: (1-{})? ".format(turn, n*n))
        try:
            move = int(move)
            if move in range(1, n*n+1):
                return move-1
            else:
                print("Not a valid move! Please try again. ")
                print_instruction(n)
        except:
            print("{} is not a valid move! Please try again. ".format(move))


def update_board(board, move, turn):
    while board[move] != -1:
        print("Invalid move! Cell already taken. Please try again.\n")
        move = get_validate_move(turn)
    board[move] = 1 if turn == 'X' else 0
    return board


def return_rows(n):
    return [[i*n+j for j in range(n)] for i in range(n)]


def return_cols(n):
    return [[i+j*n for j in range(n)] for i in range(n)]


def return_diags(n):
    main_diag = [i*(n+1) for i in range(n)]
    off_diag = [(n-1)*(i+1) for i in range(n)]
    return [main_diag, off_diag]


def generate_win_conditions(n):
    out = []
    for i in return_rows(n):
        out.append(i)
    for i in return_cols(n):
        out.append(i)
    for i in return_diags(n):
        out.append(i)
    return out


def check_win(win_conditions, n, board):
    for i in win_conditions:
        try:
            out = []
            for j in i:
                out.append(True if board[i[0]] == board[j] else False)
            if all(out):
                return board[i[0]]
        except:
            pass
    return -1


def initialise_game(n):
    board = [-1 for i in range(n*n)]
    win = False
    move = 0
    return board, win, move


def game(n):
    win_conditions = generate_win_conditions(n)
    print_instruction(n)
    board, win, move = initialise_game(n)
    while not win:
        print_board(n, board)
        print("Turn number {}".format(move+1))
        if move % 2 == 0:
            turn = "X"
        else:
            turn = "O"
        user = get_validate_move(n, turn)
        move += 1
        board = update_board(board, user, turn)
        if move > (n-1)*2:
            winner = check_win(win_conditions, n, board)
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
