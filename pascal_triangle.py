'''
Pascal's Triangle I
Easy

Given two integers r and c, return the value at the rth row and cth column (1-indexed) in a Pascal's Triangle.



In Pascal's triangle:



The first row contains a single element 1.


Each row has one more element than the previous row.


Every row starts and ends with 1.


For all interior elements (i.e., not at the ends), the value at position (r, c) is computed as the sum of the two elements directly above it from the previous row:

Pascal[r][c]=Pascal[r−1][c−1]+Pascal[r−1][c]
where indexing is 1-based
'''

# Brute Force Solution Building the Pascal's Triangle and fetching the element

class Solution:
    def pascalTriangleI(self, r, c):
        pascalT = [[1]]

        # Build the triangle row by row up to the r-th row
        # (In 0-based code terms, we loop up to index r-1)
        for i in range(1, r):
            row = []
            for j in range(i + 1):
                # The first and last elements of every row are always 1
                if j == 0 or j == i:
                    row.append(1)
                else:
                    # Sum of the two elements directly above
                    val = pascalT[i - 1][j - 1] + pascalT[i - 1][j]
                    row.append(val)

            pascalT.append(row)

        # Convert 1-based coordinates (r, c) to 0-based indices (r-1, c-1)
        return pascalT[r - 1][c - 1]


# Optimal Solution

class Solution:
    def pascalTriangleI(self, r, c):
        return self.nCr(r - 1, c - 1)

    # Function to calculate nCr
    def nCr(self, n, r):
        # Choose the smaller value for lesser iterations
        if r > n - r:
            r = n - r

        # base case
        if r == 1:
            return n

        res = 1  # to store the result

        # Calculate nCr using iterative method avoiding overflow
        for i in range(r):
            res = res * (n - i)
            res = res // (i + 1)

        return res 