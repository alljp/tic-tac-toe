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


def return_edges(size, board):
    tmp = []
    out = []
    if size % 2 != 0:
        tmp.append((size*size)//2)
    else:
        for i in [size*(size-1)//2, (size*(size-1)//2)-1,
                  size*(size+1)//2, (size*(size+1)//2)-1]:
            tmp.append(i)
    for i in [0, size-1, size*size-1, size*(size-1)]:
        tmp.append(i)
    for i in range(size*size):
        if i not in tmp:
            out.append(i)
    return out


def get_player_fork_move(size, board, turn, win_conditions):
    possibilities = 0
    for i in range(size*size):
        if board[i] == -1 and test_fork_move(
                size, board, "O" if turn == "X" else "X", i, win_conditions):
            possibilities += 1
            temp_move = i
    if possibilities == 1:
        return temp_move
    elif possibilities == 2:
        for j in return_edges(size, board):
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


def play_comp_move(size, board, move, win_conditions):
    comp_move = get_comp_move(
        size, board, utils.decide_turn(move), win_conditions)
    board = utils.update_board(
        board, comp_move, utils.decide_turn(move), size)
    return board


def next_pvc_move(size, board, move, win_conditions, is_first):
    if is_first == 1:
        board, move = utils.get_update_user_move(size, board, move)
        if move <= size*size-1:
            board = play_comp_move(size, board, move, win_conditions)
        return board, move+1
    else:
        board = play_comp_move(size, board, move, win_conditions)
        utils.print_board(size, board)
        move += 1
        if move <= size*size-1:
            board, move = utils.get_update_user_move(size, board, move)
        return board, move
