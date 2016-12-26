import convert



pgn = convert.open_pgn('train_data/acm.pgn')

board_moves = convert.generate_next_boards(pgn)

for bm in board_moves:
    print(str(bm[0]), str(bm[1]))
