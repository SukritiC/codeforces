import math


def solve():
    """
    Solves a single test case for the Left and Down problem.
    """
    a, b, k = map(int, input().split())

    # Calculate the greatest common divisor of a and b.
    g = math.gcd(a, b)

    # Determine the base move required to maintain the a:b ratio.
    # To do it in one type of move, we need to find a move (dx, dy)
    # such that (dx, dy) is a multiple of (a/g, b/g).
    # The smallest such move is (a/g, b/g) itself.
    required_dx = a // g
    required_dy = b // g

    # Check if this smallest required move is within the allowed limit k.
    if required_dx <= k and required_dy <= k:
        # If the move (a/g, b/g) is valid, we can use it 'g' times. Cost is 1.
        # It's possible to use other multiples too, but if the smallest
        # base move is not possible, no multiple of it will be possible either.
        # For example, if we need to make a move (2*required_dx, 2*required_dy),
        # it would also be > k.
        # The condition should be `max(required_dx, required_dy) <= k`.
        # Oh, wait. Let's reconsider the case a=12, b=18, k=8.
        # g=6, req_dx=2, req_dy=3. k>=max(2,3) -> k>=3 -> 8>=3. YES. Cost 1.
        # What if k=2? Then k>=max(2,3) is false. Cost 2. Correct.
        # What if a=12,b=18,k=5. g=6, req_dx=2, req_dy=3.
        # We can use move (2,3) 6 times if k>=3.
        # We can use move (4,6) 3 times if k>=6. k=5, so no.
        # We can use move (6,9) 2 times if k>=9. k=5, so no.
        # We can use move (12,18) 1 time if k>=18. k=5, so no.
        # The smallest required dx,dy are a/g and b/g.
        # Let's check the other side: we need to cover `a` and `b`
        # with moves (dx,dy). We need to find if there exists a common divisor `c` of `a` and `b`
        # such that a/c <= k and b/c <= k.
        # This is equivalent to c >= a/k and c >= b/k.
        # We only need to check the largest common divisor, which is g.
        # So the condition is g >= a/k and g >= b/k, which is k*g >= a and k*g >= b.
        # This is equivalent to k >= a/g and k >= b/g. My original logic was correct.

        # We are checking if k is large enough for the SMALLEST possible move vector
        # that is proportional to (a, b). That vector is (a/g, b/g).
        # Any other valid single move would be (m*a/g, m*b/g), which would
        # require an even larger k.

        # Also need to check if the OTHER required move is valid
        # Let's check max(a,b)/g vs k
        if max(a, b) // g < k:
            print(1)
        # What if a=6,b=10,k=4. g=2. a/g=3, b/g=5. k    >=5 is false. cost=2.
        # With my new check: max(6,10)/2=5. 5<4 is false. This seems wrong.
        # Let's stick to the original logic which passed all examples.
        elif a // g < k and b // g < k:
            print(1)
        else:  # The case where one of them equals k
            # Let a=4, b=6, k=3. g=2. a/g=2, b/g=3. k>=2 and k>=3. 3>=3 holds. Cost 1.
            # My code: 2<3 and 3<3 is false.
            # The condition is <=, not <
            if max(a // g, b // g) <= k:
                print(1)
            else:
                print(2)
    else:
        # If the smallest required move is not possible, then no single type of
        # move can solve it. We must use at least two. We can always solve it
        # with two moves: (1, 0) and (0, 1), since k >= 1.
        print(2)


# Read the number of test cases
try:
    num_test_cases = int(input())
    for _ in range(num_test_cases):
        solve()
except (IOError, EOFError):
    pass
