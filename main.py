import convert
import random

import tensorflow as tf
import tensorflow.contrib as tfc

from tensorflow.contrib.learn import DNNRegressor, SKCompat


random.seed(0xbedbeef)  # so we get consistent results

fit_boards = []
fit_moves = []

with open('train_data/acm.pgn') as pgn:
    boards, moves = convert.generate_next_boards(pgn)

    fit_boards += boards
    fit_moves += moves


target_boards = []

with open('train_data/man_machine.pgn') as pgn:
    boards, moves = convert.generate_next_boards(pgn)

    target_boards += boards


nn = SKCompat(DNNRegressor(hidden_units=[64, 128, 63],
                  feature_columns=[tfc.layers.real_valued_column("")]))


nn.fit(tf.constant(fit_boards), tf.constant(fit_moves))

res = nn.predict(target_boards)

print(res)

