from copy import deepcopy
import math
import time
import urllib.request
import urllib.error
import numpy as np
import os

class Board:
    
    def __init__(self, dimension, board_matrix, constraints_dic):
        self.dimension = dimension
        self.board_matrix = board_matrix
        self.constraints_dic = constraints_dic
          
    def find_constraints(self):
        
        table_dic = {}   
        for i in range(self.dimension):
            for j in range(self.dimension):
                if self.board_matrix[i][j] != -1:
                    table_dic[(i, j)] = self.find_position(i, j) 
                    
        self.table_dic = table_dic
        return table_dic
          
    def find_position(self, i, j):
        col_up = 0
        col_down = 0
        row_up = 0
        row_down = 0
        
        co_i = i
        co_j = j
        while (self.board_matrix[co_i][co_j] != -1):
            co_i -= 1
        col_up = co_i
        co_i = i
        
        while (co_i <= self.dimension-1 and self.board_matrix[co_i][co_j] != -1):
            co_i += 1 
        col_down = co_i
        co_i = i
        
        while (self.board_matrix[co_i][co_j] != -1):
            co_j -= 1
        row_up = co_j
        co_j = j
        
        while (co_j <= self.dimension-1 and self.board_matrix[co_i][co_j] != -1):
            co_j += 1
        row_down = co_j
        
        return (col_up, row_up), (col_down, row_down)      
    
    def move_to_next_cell(self, i, j):
        j += 1
        if j >= self.dimension:
            j %= self.dimension
            i += 1
            if i >= self.dimension:
                if 0 in self.board_matrix:
                    index = np.where(np.array(self.board_matrix) == 0)
                    i = index[0][0]
                    j = index[1][0]
                
        return i, j
    
    def back_tracking(self, i, j, show):

        if i >= self.dimension or j >= self.dimension:
            return True
        
        while self.board_matrix[i][j] != 0:
            i, j = self.move_to_next_cell(i, j)
            if i >= self.dimension or j >= self.dimension:
                return True
        
        for value in self.possible_values(i, j):
            self.board_matrix[i][j] = value
            if show == True:
                os.system('clear')
                self.display(self.board_matrix)
                time.sleep(0.2)
            p, q = self.move_to_next_cell(i, j)
            if self.back_tracking(p, q, show):
                return True
        self.board_matrix[i][j] = 0
        
        return False
    
    def possible_values(self, i, j):
        
        possible = []
        constriant_index = self.table_dic[(i, j)]
        col_constriant = self.constraints_dic.get((constriant_index[0][0], j))[0]
        row_constriant = self.constraints_dic.get((i, constriant_index[0][1]))[1]
        range_i = constriant_index[1][0]
        range_j = constriant_index[1][1]
        row_sum = sum(self.board_matrix[i,constriant_index[0][1]+1:range_j])
        col_sum = sum(self.board_matrix[constriant_index[0][0]+1:range_i,j])
        
        for c in range(1, 10): 
            if c not in self.board_matrix[constriant_index[0][0]+1:range_i,j] and c not in self.board_matrix[i,constriant_index[0][1]+1:range_j] and row_sum+c <= row_constriant and col_sum+c <= col_constriant:
                self.board_matrix[i][j] = c
                if 0 not in self.board_matrix[constriant_index[0][0]+1:range_i,j]:
                    if col_sum+c == col_constriant:
                        possible.append(c)
                    continue
                if 0 not in self.board_matrix[i,constriant_index[0][1]+1:range_j]:
                    if row_sum+c == row_constriant:
                        possible.append(c)
                if 0 in self.board_matrix[constriant_index[0][0]+1:range_i,j] and 0 in self.board_matrix[i,constriant_index[0][1]+1:range_j]:
                    possible.append(c)
                self.board_matrix[i][j] = 0 
                    
        
             
        return possible
    
    def display(self, board):
        
        for i in range(self.dimension):
            for j in range(self.dimension):
                
                c = self.constraints_dic.get((i, j))
                
                if board[i][j] == -1 and c != None:
                    free = 7 - (len(str(c[0])) + len(str(c[1])) + 1)
                    print( (" "*math.ceil(free/2)) + str(c[0]) + "/" + str(c[1]) + (" "*math.floor(free/2)) + "|", end="")
                elif board[i][j] == -1 and c == None:
                    print("   X   |", end="")
                else:
                    print("   " + str(board[i][j]) + "   |", end="")
            print()
        print(" ")
    
    def choosing_start(self):
        
        m = self.dimension*2
        value = None
        
        for i in range(self.dimension):
            for j in range(self.dimension):
                if self.board_matrix[i][j] != -1:
                    
                    constriant_index = self.table_dic[(i, j)]
                    col_constriant = self.constraints_dic.get((constriant_index[0][0], j))[0]
                    row_constriant = self.constraints_dic.get((i, constriant_index[0][1]))[1]
                    o = col_constriant + row_constriant
                    if o < m:
                        m = o
                        value = (i, j)
            
        return value                
    
    def solve(self, i, j, show):
        
        self.find_constraints()
        if i == -1 and j == -1:
            start = self.choosing_start()
            print("Starting point: ", start)
            self.back_tracking(start[0], start[1], show)
        else:
            self.back_tracking(i, j, show)
        self.display(self.board_matrix)       
        
        
   
        
                    
                
            
            
            