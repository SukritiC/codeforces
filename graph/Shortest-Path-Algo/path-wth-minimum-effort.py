import heapq


class Solution:
    # Delta row and column array
    delRow = [-1, 0, 1, 0]
    delCol = [0, -1, 0, 1]

    # Function to check if a cell is valid
    def isValid(self, row, col, n, m):
        # Return false if the cell is invalid
        if row < 0 or row >= n: return False
        if col < 0 or col >= m: return False

        # Return true if the cell is valid
        return True

    # Function to determine minimum efforts
    # to go from top-left to bottom-right
    def MinimumEffort(self, heights):

        # Get the dimensions of grid
        n = len(heights)
        m = len(heights[0])

        # To store maximum difference
        maxDiff = [[float('inf')] * m for _ in range(n)]

        # Min-Heap storing the pair:
        # {diff, {row of cell, column of cell}}
        pq = []

        # Mark the initial position as 0
        maxDiff[0][0] = 0

        # Push the starting cell to min-heap
        heapq.heappush(pq, (0, 0, 0))

        # Until the min-heap is not empty
        while pq:

            # Get the cell with minimum
            # difference (effort)
            diff, row, col = heapq.heappop(pq)

            # If the destination cell is reached,
            # return the difference
            if row == n - 1 and col == m - 1:
                return diff

            # Traverse its neighbors
            for i in range(4):

                # Get the coordinates
                # of neighboring cell
                newRow = row + self.delRow[i]
                newCol = col + self.delCol[i]

                # Check if the cell is valid
                if self.isValid(newRow, newCol, n, m):

                    # Get the current difference
                    # in heights of cells
                    currDiff = abs(heights[newRow][newCol] -
                                   heights[row][col])

                    # Check if the current difference is
                    # less than earlier known difference
                    if (max(currDiff, diff) <
                            maxDiff[newRow][newCol]):
                        # Store the current difference
                        maxDiff[newRow][newCol] = max(currDiff, diff)

                        # Add the new pair found in the min-heap
                        heapq.heappush(pq, (max(currDiff, diff), newRow, newCol))

        # Return -1
        return -1


# Example usage
if __name__ == "__main__":
    heights = [
        [1, 2, 2],
        [3, 8, 2],
        [5, 3, 5]
    ]

    # Creating an instance of Solution class
    sol = Solution()

    # Function call to determine minimum efforts
    # to go from top-left to bottom-right
    ans = sol.MinimumEffort(heights)

    # Output
    print(f"The minimum efforts required to go from cell (0,0) to cell (row-1, col-1) is: {ans}")
