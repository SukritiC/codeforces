'''
Problem Title: The Balanced Archive Sequence

Background: A global logistics company, Wonder Solutions, uses a unique identification system for their warehouse bins.
Each bin is assigned a weight value. For a specific zone, the system requires a sequence of n distinct weight values
where the absolute values of these weights must be a complete set of integers from 1 to n (a permutation).

The Challenge:
To optimize the automated sorting robots, the system needs to generate a sequence that meets a
specific "Stability Goal." The sum of all values in the sequence must exactly equal a given target_sum.
Because the robots process items from left to right, they are most efficient when they encounter smaller values first.
Therefore, if multiple sequences satisfy the requirements, the system must output the lexicographically smallest one.

DefinitionsPermutation Requirement:
The absolute values of the sequence must contain every number from 1 to size exactly once. (e.g., if size is 3,
the absolute values must be {1, 2, 3}).

Lexicographically Smallest: Sequence A is smaller than Sequence B if, at the first position where they differ,
the value in A is less than the value in B. (e.g., [-3, 1, 2] is smaller than [-3, 2, 1]).

Task : Write a function findOptimalSequence that takes:
    int size: The number of elements required.
    long target_sum: The required total sum of the elements.

Returns : An array of size integers representing the lexicographically smallest valid sequence.
If no such sequence exists, return an array of size zeros.

'''



def flipped_arrays_optimized(arr, target_sum, size):
    initial_sum = sum(arr)
    diff = target_sum - initial_sum

    # Same parity check: the gap must be even to be solved by flipping
    if diff < 0 or diff % 2 != 0:
        return [0]*size

    subset_target = diff // 2

    # map: {sum_value: [list_of_index_combinations]}
    # We start knowing that a sum of 0 is achieved by an empty group []
    dp = {0: [[]]}

    # Only negative numbers can be flipped to increase the sum
    for i, val in enumerate(arr):
        if val < 0:
            num = abs(val)
            new_sums = {}

            for current_sum, combos in dp.items():
                new_sum = current_sum + num
                if new_sum <= subset_target:
                    # For every way we reached 'current_sum',
                    # we can now reach 'new_sum' by adding index 'i'
                    if new_sum not in new_sums:
                        new_sums[new_sum] = []

                    for combo in combos:
                        new_sums[new_sum].append(combo + [i])

            # Merge new sums back into our main DP table
            for s, c in new_sums.items():
                if s not in dp:
                    dp[s] = []
                dp[s].extend(c)

    # 3. Build the final arrays from the successful index groups
    results = []
    if subset_target in dp:
        for indices in dp[subset_target]:
            # Create the new array by flipping the chosen indices
            new_arr = list(arr)
            for idx in indices:
                new_arr[idx] = abs(new_arr[idx])

            # 1. Sort the new_arr
            new_arr.sort()

            # 2. Conditional replacement logic
            if not results:
                # If results is empty, just add the first one we find
                results.extend(new_arr)
            else:
                # Check if the 0th element of the new_arr is better (smaller)
                # than the 0th element of what we already found.
                # Note: We compare against results[0] assuming you want
                # to track the "best" version found so far.
                if new_arr[0] < results[0]:
                    results = new_arr  # Replace existing with the better one
                elif new_arr[0] == results[0]:
                    # If they are equal, you might want to keep both?
                    # If not, just do nothing (skip).
                    pass



    return results


if __name__ == "__main__":
    size = 5
    target_sum = 9

    arr = [-i for i in range(1,size+1)]

    result =  flipped_arrays_optimized(arr, target_sum, size)

    print(result)