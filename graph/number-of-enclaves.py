from collections import deque


class Solution:
    def __init__(self):
        self.delRow = [-1, 0, 1, 0]
        self.delCol = [0, 1, 0, -1]

    # Helper Function to check if a
    # cell is within boundaries
    def isValid(self, i, j, n, m):

        # Return false if cell is invalid
        if i < 0 or i >= n:
            return False
        if j < 0 or j >= m:
            return False

        # Return true if cell is valid
        return True

    # Function to perform BFS traversal
    def bfs(self, grid, q, vis):

        # Getting the dimensions of image
        n = len(grid)
        m = len(grid[0])

        # Until the queue is empty
        while q:
            # Get the cell from queue
            cell = q.popleft()

            # Get its coordinates
            row, col = cell

            # Traverse its 4 neighbors
            for i in range(4):

                # Coordinates of new cell
                nRow = row + self.delRow[i]
                nCol = col + self.delCol[i]

                # check for valid, unvisited
                # and land cells
                if (self.isValid(nRow, nCol, n, m) and
                        grid[nRow][nCol] == 1 and
                        vis[nRow][nCol] == False):
                    # Mark the new cell as visited
                    # and add it to the queue
                    vis[nRow][nCol] = True
                    q.append((nRow, nCol))

    # Function to find number of enclaves
    def numberOfEnclaves(self, grid):

        # Get the dimensions of grid
        n = len(grid)
        m = len(grid[0])

        # Queue for BFS traversal
        q = deque()

        # Visited array
        vis = [[False] * m for _ in range(n)]

        # Traverse the grid and add
        # the border land cells to queue
        for i in range(n):
            for j in range(m):

                # If the land cell is at
                # border, add it to queue
                if ((i == 0 or i == n - 1 or
                     j == 0 or j == m - 1) and
                        grid[i][j] == 1):
                    vis[i][j] = True
                    q.append((i, j))

        # Perform the bfs traversal
        # from border land cells
        self.bfs(grid, q, vis)

        # Count to store number of enclaves
        count = 0

        # Traverse the grid
        for i in range(n):
            for j in range(m):

                # If cell is a land cell and
                # unvisited, update the count
                if grid[i][j] == 1 and not vis[i][j]:
                    count += 1

        # Return count as answer
        return count