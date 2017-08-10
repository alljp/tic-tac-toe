import utils


def test_move_win(size, board, turn, move, win_conditions):
    board_copy = board[:]
    utils.update_board(board_copy, move, turn, size)
    return False if utils.check_win(win_conditions, board_copy) == -1 else True


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


def test_fork_move(size, board, turn, move, win_conditions):
    board_copy = board[:]
    utils.update_board(board_copy, move, turn, size)
    possibilities = 0
    for j in range(0, size*size):
        if board_copy[j] == -1 and test_move_win(
                size, board_copy, turn, j, win_conditions):
            possibilities += 1
    return possibilities >= 2


def get_comp_fork_move(size, board, turn, win_conditions):
    for i in range(size*size):
        if board[i] == -1 and test_fork_move(
                size, board, turn, i, win_conditions):
            return i


def get_player_fork_move(size, board, turn, win_conditions):
    possibilities = 0
    for i in range(size*size):
        if board[i] == -1 and test_fork_move(
                size, board, "O" if turn == "X" else "X", i, win_conditions):
            possibilities += 1
            temp_move = i
    if possibilities == 1:
        return temp_move
    elif possibilities > 1:
        for j in [1, 3, 5, 7]:
            if board[j] == -1:
                return j


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
    out.append(get_comp_fork_move(size, board, turn, win_conditions))
    out.append(get_player_fork_move(size, board, turn, win_conditions))
    out.append(get_corner_cell(size, board))
    out.append(get_any_cell(size, board))
    for i in out:
        if i is not None:
            return i


def next_pvc_move(size, board, move, win_conditions):
    turn = utils.decide_turn(move)
    user = utils.get_validate_move(size, turn)
    move += 1
    board = utils.update_board(board, user, turn, size)
    if move <= size*size-1:
        comp_move = get_comp_move(
            size, board, utils.decide_turn(move), win_conditions)
        board = utils.update_board(
            board, comp_move, utils.decide_turn(move), size)
    return board, move+1
