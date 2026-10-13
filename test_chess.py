from chess_logic import new_board

def test_board_is_8_by_8():
    board = new_board()
    assert len(board) == 8
    for row in board:
        assert len(row) == 8