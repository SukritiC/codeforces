import sys


def solve():
    """
    Solves a single test case for the Prefix Min and Suffix Max problem.
    """
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))

    if n == 0:
        print("")
        return

    # 1. Precompute prefix minimums
    prefix_min = [0] * n
    prefix_min[0] = a[0]
    for i in range(1, n):
        prefix_min[i] = min(prefix_min[i - 1], a[i])

    # 2. Precompute suffix maximums
    suffix_max = [0] * n
    suffix_max[n - 1] = a[n - 1]
    for i in range(n - 2, -1, -1):
        suffix_max[i] = max(suffix_max[i + 1], a[i])

    # 3. Build the result string
    result = []
    for i in range(n):
        # Get min of prefix to the left and max of suffix to the right
        # Use float('inf') and float('-inf') for edge cases i=0 and i=n-1
        min_left = prefix_min[i - 1] if i > 0 else float('inf')
        max_right = suffix_max[i + 1] if i < n - 1 else float('-inf')

        if a[i] < min_left or a[i] > max_right:
            result.append('1')
        else:
            result.append('0')

    print("".join(result))


# Read the number of test cases and run the solver
try:
    num_test_cases = int(sys.stdin.readline())
    for _ in range(num_test_cases):
        solve()
except (IOError, ValueError):
    # Handle potential empty input or format errors
    pass

