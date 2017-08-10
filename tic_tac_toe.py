def print_cell_value(char):
    return " {}".format(char) if len(str(char)) < 2 else "{}".format(char)


def print_row_seperator(num):
    return "-----"*num


def print_board(size, board):
    for i in range(size):
        print(" ", end="")
        for j in range(size):
            if board[i*size+j] == 1:
                print(print_cell_value("X"), end="")
            elif board[i*size+j] == 0:
                print(print_cell_value("O"), end="")
            else:
                print(print_cell_value(" "), end="")
            if j != size-1:
                print(" | ", end="")
        print()
        if i != size-1:
            print(print_row_seperator(size))
        else:
            print()


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


def return_rows(size):
    return [[i*size+j for j in range(size)] for i in range(size)]


def return_cols(size):
    return [[i+j*size for j in range(size)] for i in range(size)]


def return_diags(size):
    main_diag = [i*(size+1) for i in range(size)]
    off_diag = [(size-1)*(i+1) for i in range(size)]
    return [main_diag, off_diag]


def generate_win_conditions(size):
    out = []
    for i in return_rows(size):
        out.append(i)
    for i in return_cols(size):
        out.append(i)
    for i in return_diags(size):
        out.append(i)
    return out


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


def decide_winner(win_conditions, size, board, move):
    winner = check_win(win_conditions, board)
    if winner != -1:
        print("The winner is {}".format("X" if winner == 1 else "O"))
        return True
    elif move == size*size:
        print("No winner")
        return True


def next_move(size, board, move):
    turn = decide_turn(move)
    user = get_validate_move(size, turn)
    move += 1
    board = update_board(board, user, turn, size)
    return board, move


def decide_turn(move):
    return "X" if move % 2 == 0 else "O"


def initialise_game(size):
    board = [-1 for i in range(size*size)]
    win = False
    move = 0
    return board, win, move


def test_move_win(size, board, turn, move, win_conditions):
    board_copy = board[:]
    update_board(board_copy, move, turn, size)
    return False if check_win(win_conditions, board_copy) == -1 else True


def comp_win_move(size, board, turn, win_conditions):
    for i in range(0, size*size):
        if board[i] == -1 and test_move_win(
                size, board, turn, i, win_conditions):
            return i


def player_win_move(size, board, turn, win_conditions):
    for i in range(0, size*size):
        if board[i] == -1 and test_move_win(
                size, board, "O" if turn == "X" else "X", i, win_conditions):
            return i


def get_mid_cell(size, board):
    if size % 2 != 0:
        if board[(size*size)//2] == -1:
            return (size*size)//2
    else:
        for i in [size*(size-1)//2, (size*(size-1)//2)-1,
                  size*(size+1)//2, (size*(size+1)//2)-1]:
            if board[i] == -1:
                return i


def get_corner_cell(size, board):
    for i in [0, size-1, size*size-1, size*(size-1)]:
        if board[i] == -1:
            return i


def get_any_cell(size, board):
    for i in range(0, size*size):
        if board[i] == -1:
            return i


def get_comp_move(size, board, turn, win_conditions):
    out = []
    out.append(comp_win_move(size, board, turn, win_conditions))
    out.append(player_win_move(size, board, turn, win_conditions))
    out.append(get_mid_cell(size, board))
    out.append(get_corner_cell(size, board))
    out.append(get_any_cell(size, board))
    for i in out:
        if i is not None:
            return i


def next_pvc_move(size, board, move, win_conditions):
    turn = decide_turn(move)
    user = get_validate_move(size, turn)
    move += 1
    board = update_board(board, user, turn, size)
    if move < size*size-1:
        comp_move = get_comp_move(
            size, board, decide_turn(move), win_conditions)
        board = update_board(board, comp_move, decide_turn(move), size)
    return board, move+1


def game(size, opt):
    win_conditions = generate_win_conditions(size)
    print_instruction(size)
    board, win, move = initialise_game(size)
    print_board(size, board)
    while not win:
        print("Turn number {}".format(move+1))
        if opt == 1:
            board, move = next_move(size, board, move)
        else:
            board, move = next_pvc_move(size, board, move, win_conditions)
        print_board(size, board)
        if move > (size-1)*2:
            win = decide_winner(win_conditions, size, board, move)


def main():
    while True:
        size = int(input("Enter board size: "))
        opt = int(input("""How do you want to play?
                1.Player vs Player
                2.Player vs Computer"""))
        game(size, opt)
        if input("Start a new game? (y/n)").lower() != 'y':
            break


if __name__ == "__main__":
    main()
