import numpy as np
from chess.pgn import read_game

WHITE_VALUES = {
    'p': 1,
    'P': -1,
    'n': 3,
    'N': -3,
    'b': 4,
    'B': -4,
    'r': 6,
    'R': -6,
    'q': 12,
    'Q': -12,
    'k': 100,
    'K': -100
}

BLACK_VALUES = {k: v*-1 for k,v in WHITE_VALUES.items() }


def fen_to_array(board):
    fen = board.fen()
    (pieces, turn, _) = fen.split(' ', 2)

    if turn == 'b':
        VALUES = WHITE_VALUES
    else:
        VALUES = BLACK_VALUES

    ret = np.zeros((8,8), dtype=np.int)

    row = 0
    col = 0

    for piece in pieces:
        if piece.isnumeric():
            col += int(piece)
        elif piece == '/':
            row += 1
            col = 0
        else:
            ret[row, col] = VALUES[piece]
            col += 1

    return ret


def move_to_int(move):
    return (move.from_square << 8) + move.to_square


def generate_next_boards(pgn_handle):
    game = read_game(pgn_handle)

    variations = game.variations

    count = 1

    boards = []
    moves = []

    while variations:
        # print(str(count) + ": " + str(variations[0].move))

        array = fen_to_array(variations[0].board())

        # print(array)

        variations = variations[0].variations
        count += 1

        if variations:
            move = move_to_int(variations[0].move)
            boards.append(array)
            moves.append(move)

    return boards, moves

