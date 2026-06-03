'''
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0. You must do it in place.
'''

import sys

INT_MAX = sys.maxsize

class Solution:
    def setZeroes(self, matrix):
        n = len(matrix)
        m = len(matrix[0])
        for i in range(0, n):
            for j in range(0, m):
                if matrix[i][j] == 0:
                    for k in range(0, m):
                        if matrix[i][k] != 0:
                            matrix[i][k] = INT_MAX
                    for k in range(0, n):
                        if matrix[k][j] != 0:
                            matrix[k][j] = INT_MAX

        for i in range(0, n):
            for j in range(0, m):
                if matrix[i][j] == INT_MAX:
                    matrix[i][j] = 0




