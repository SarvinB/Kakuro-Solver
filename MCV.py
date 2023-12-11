
from MCVBoard import MCVBoard
import numpy as np
import timeit


dimension = 10
board_matrix = np.zeros((dimension, dimension), int)
for i in range(dimension):
    board_matrix[0][i] = -1
    board_matrix[i][0] = -1

#Expert
board_matrix[1][1] = -1
board_matrix[1][2] = -1
board_matrix[1][5] = -1
board_matrix[1][6] = -1
board_matrix[1][9] = -1
board_matrix[2][5] = -1
board_matrix[2][6] = -1
board_matrix[3][3] = -1
board_matrix[4][1] = -1
board_matrix[4][4] = -1
board_matrix[4][7] = -1
board_matrix[5][1] = -1
board_matrix[5][4] = -1
board_matrix[5][5] = -1
board_matrix[5][6] = -1
board_matrix[5][9] = -1
board_matrix[6][3] = -1
board_matrix[6][6] = -1
board_matrix[6][9] = -1
board_matrix[7][7] = -1
board_matrix[8][4] = -1
board_matrix[8][5] = -1
board_matrix[9][1] = -1
board_matrix[9][4] = -1
board_matrix[9][5] = -1
board_matrix[9][8] = -1
board_matrix[9][9] = -1

dic = {(0, 3):(17, 0), (0, 4):(19, 0), (0, 7):(7, 0), (0, 8):(44, 0),
 (1, 1):(3, 0), (1, 2):(37, 17), (1, 6):(0, 10), (1, 9):(23, 0),
 (2, 0):(0, 20), (2, 5):(6, 0), (2, 6):(3, 15), (3, 0):(0, 5), (3, 3):(3, 25),
 (4, 1):(0, 8), (4, 4):(0, 3), (4, 7):(10, 15), (5, 1):(13, 3), 
 (5, 4):(7, 0), (5, 5):(5, 0), (5, 6):(0, 17), (6, 0):(0, 9), (6, 3):(10, 3),
 (6, 6):(16, 6), (6, 9):(11, 0), (7, 0):(0, 38), (7, 7):(3, 17),
 (8, 0):(0, 7), (8, 5):(0, 12), (9, 1):(0, 4), (9, 5):(0, 3)}


start = timeit.default_timer()

board = MCVBoard(dimension, np.array(board_matrix), dic)
board.solve(7, 6, False)

stop = timeit.default_timer()

print('Time: ', stop - start)