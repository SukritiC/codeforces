class Solution:
    def solve(self, bt):
        bt.sort()

        # Initialize total waiting time
        wait_time = 0
        # Initialize total time taken
        total_time = 0
        # Get number of jobs
        n = len(bt)

        # Iterate to calculate waiting time
        for i in range(n):
            wait_time += total_time
            total_time += bt[i]

        # Return average waiting time
        return wait_time // n