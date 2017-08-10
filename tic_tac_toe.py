from engine import next_pvc_move
import utils


def print_board(size, board):
    for i in range(size):
        print(" ", end="")
        for j in range(size):
            if board[i*size+j] == 1:
                print(utils.print_cell_value("X"), end="")
            elif board[i*size+j] == 0:
                print(utils.print_cell_value("O"), end="")
            else:
                print(utils.print_cell_value(" "), end="")
            if j != size-1:
                print(" | ", end="")
        print()
        if i != size-1:
            print(utils.print_row_seperator(size))
        else:
            print()


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


def decide_winner(win_conditions, size, board, move):
    winner = utils.check_win(win_conditions, board)
    if winner != -1:
        print("The winner is {}".format("X" if winner == 1 else "O"))
        return True
    elif move == size*size:
        print("No winner")
        return True


def next_move(size, board, move):
    turn = utils.decide_turn(move)
    user = utils.get_validate_move(size, turn)
    move += 1
    board = utils.update_board(board, user, turn, size)
    return board, move


def initialise_game(size):
    board = [-1 for i in range(size*size)]
    win = False
    move = 0
    return board, win, move


def game(size, opt):
    win_conditions = generate_win_conditions(size)
    utils.print_instruction(size)
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
