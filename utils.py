def print_cell_value(char):
    return " {}".format(char) if len(str(char)) < 2 else "{}".format(char)


def print_row_seperator(num):
    return "-----"*num


def print_instruction(size):
    print("Please use the following cell numbers to make your move")
    for i in range(size):
        print(print_cell_value(" "), end="")
        for j in range(size):
            print(print_cell_value(i*size+j+1), end="")
            if j != size-1:
                print(" | ", end="")
        print()
        if i != size-1:
            print(print_row_seperator(size))
        else:
            print()


def get_validate_move(size, turn):
    while True:
        move = input(
            "Where would you like to place {}: (1-{})? ".format(turn,
                                                                size*size))
        try:
            move = int(move)
            if move in range(1, size*size+1):
                return move-1
            else:
                print("Not a valid move! Please try again. ")
                print_instruction(size)
        except:
            print("{} is not a valid move! Please try again. ".format(move))


def update_board(board, move, turn, size):
    while board[move] != -1:
        print("Invalid move! Cell already taken. Please try again.\n")
        move = get_validate_move(size, turn)
    board[move] = 1 if turn == 'X' else 0
    return board


def decide_turn(move):
    return "X" if move % 2 == 0 else "O"


def check_win(win_conditions, board):
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
