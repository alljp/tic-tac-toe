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


def main():
    print_instruction()


if __name__ == "__main__":
    main()
