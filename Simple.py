from SimpleBoard import Board
import numpy as np
import timeit

#Enter dimention of board
dimension = 10
board_matrix = np.zeros((dimension, dimension), int)
for i in range(dimension):
    board_matrix[0][i] = -1
    board_matrix[i][0] = -1
    
#Hard
board_matrix[1][1] = -1
board_matrix[1][2] = -1
board_matrix[1][5] = -1
board_matrix[1][8] = -1
board_matrix[1][9] = -1
board_matrix[2][1] = -1
board_matrix[2][9] = -1
board_matrix[3][3] = -1
board_matrix[3][7] = -1
board_matrix[4][4] = -1
board_matrix[4][5] = -1
board_matrix[4][6] = -1
board_matrix[5][1] = -1
board_matrix[5][4] = -1
board_matrix[5][5] = -1
board_matrix[5][6] = -1
board_matrix[5][9] = -1
board_matrix[6][4] = -1
board_matrix[6][5] = -1
board_matrix[6][6] = -1
board_matrix[7][3] = -1
board_matrix[7][7] = -1
board_matrix[8][1] = -1
board_matrix[8][9] = -1
board_matrix[9][1] = -1
board_matrix[9][2] = -1
board_matrix[9][5] = -1
board_matrix[9][8] = -1
board_matrix[9][9] = -1

dic = {(0, 3):(15, 0), (0, 4):(6, 0), (0, 6):(21, 0), (0, 7):(12, 0),
 (1, 2):(42, 10), (1, 5):(16, 16), (1, 8):(31, 0),
 (2, 1):(16, 42), (2, 9):(3, 0), (3, 0):(0, 16), (3, 3):(6, 19), (3, 7):(7, 5),
 (4, 0):(0, 17), (4, 6):(0, 7), (5, 1):(3, 9), (5, 6):(0, 3), (5, 9):(10, 0),
 (6, 0):(0, 7), (6, 4):(24, 0), (6, 5):(12, 0), (6, 6):(24, 6),
 (7, 0):(0, 4), (7, 3):(3, 24), (7, 7):(15, 15), (8, 1):(0, 39), 
 (9, 2):(0, 11), (9, 5):(0, 16)}



start = timeit.default_timer()

board = Board(dimension, np.array(board_matrix), dic)
board.solve(-1, -1, False)

stop = timeit.default_timer()

print('Time: ', stop - start)