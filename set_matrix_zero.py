'''
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0. You must do it in place.
'''

# Brute Force

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

# Better solution

class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        n = len(matrix)
        m = len(matrix[0])

        # Track which rows and columns should be zeroed
        zero_rows = [False] * n
        zero_cols = [False] * m

        # Step 1: First pass to identify all rows and columns with zeros
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    zero_rows[i] = True
                    zero_cols[j] = True

        # Step 2: Second pass to update the matrix
        for i in range(n):
            for j in range(m):
                if zero_rows[i] or zero_cols[j]:
                    matrix[i][j] = 0


# Optimal Solution

class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        n = len(matrix)
        m = len(matrix[0])
        col0 = 1  # Track if the first column needs to be zeroed

        # Step 1: Use the first row and column as markers
        for i in range(n):
            if matrix[i][0] == 0:
                col0 = 0
            for j in range(1, m):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # Step 2: Iterate backwards to update the matrix
        # (skipping the first row and column for now)
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, 0, -1):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
            # Update the first column element
            if col0 == 0:
                matrix[i][0] = 0


