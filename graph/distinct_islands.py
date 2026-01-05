from typing import List


class Solution:
    # DelRow and delCol for neighbors
    delRow = [-1, 0, 1, 0]
    delCol = [0, -1, 0, 1]

    def isValid(self, i, j, n, m):

        if i < 0 or i >= n: return False
        if j < 0 or j >= m: return False

        return True


    def dfs(self, row, col, grid, visited,
            path, base_row, base_col):

        n = len(grid)
        m = len(grid[0])
        path.append((row - base_row, col - base_col))
        for i in range(4):

            nRow = row + self.delRow[i]
            nCol = col + self.delCol[i]
            if (self.isValid(nRow, nCol, n, m) and
                    grid[nRow][nCol] == 1 and
                    not visited[nRow][nCol]):
                visited[nRow][nCol] = True
                self.dfs(nRow, nCol, grid, visited,
                         path, base_row, base_col)
        return


    def countDistinctIslands(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        visited = [[False for _ in range(m)] for _ in range(n)]
        st = set()
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and not visited[i][j]:
                    visited[i][j] = True
                    path = []
                    self.dfs(i, j, grid, visited, path, i, j)
                    st.add(tuple(path))

        return len(st)


# Example usage
grid = [
    [1, 1, 0, 1, 1],
    [1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1],
    [1, 1, 0, 1, 1]
]

# Creating an instance of Solution class
sol = Solution()

# Function to count the count of distinct islands in the given grid
ans = sol.countDistinctIslands(grid)

# Output
print("The count of distinct islands in the given grid is:", ans)
