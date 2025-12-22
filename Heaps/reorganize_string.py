
import heapq
from collections import Counter

def reorganizeString(s: str) -> str:
    # Step 1: Count frequencies
    freq = Counter(s)

    # Step 2: Build a max heap
    # Python has min-heap, so we push negative counts
    max_heap = [(-count, char) for char, count in freq.items()]
    heapq.heapify(max_heap)

    prev_count, prev_char = 0, ''
    result = []

    # Step 3: Greedy placement
    while max_heap:
        count, char = heapq.heappop(max_heap)
        result.append(char)

        # Push previous character back if it still has remaining count
        if prev_count < 0:
            heapq.heappush(max_heap, (prev_count, prev_char))

        # Update current character count
        count += 1  # because count is negative
        prev_count, prev_char = count, char

    # Step 4: Validate result length
    return "".join(result) if len(result) == len(s) else ""


if __name__ == "__main__":
    print(reorganizeString("aab"))    # Output: "aba"
    print(reorganizeString("aaab"))   # Output: ""

# Brute Force

if __name__ == "__main__":
    str1 = "aab"
    str2 = "aaab"

    n = len(str2)
    str_lst = []
    for s in str2:
        str_lst.append(s)
    alpha = []

    # print(str_lst)
    for i in range(n):
        if str_lst[i] not in alpha:
            alpha.append(str1[i])
        else:
            for j in range(i+1, n):
                if str_lst[j] not in alpha:
                    str_lst[i], str_lst[j] = str_lst[j], str_lst[i]
                    break


    flag = 0
    for i in range(1, n):
        if str_lst[i] == str_lst[i-1]:
            flag = 1
            break
    if flag == 0:
        print(str_lst)
    else:
        print("")