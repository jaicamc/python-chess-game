def new_board():
    back_rank = ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"]
    black_pawns = ["bP"] * 8
    empty_row = ["--"] * 8
    white_pawns = ["wP"] * 8
    white_back_rank = ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]

    board = [
        back_rank,
        black_pawns, empty_row, empty_row, empty_row, empty_row, white_pawns, white_back_rank
    ]
    return board


def print_board(board):
    for row in board:
        print(" ".join(row))


if __name__ == "__main__":
    board = new_board()
    print_board(board)

