'''
Scenario: You are building the Fraud Detection System for a credit card processor. We process a continuous stream of transactions. For each transaction, we receive an amount. To detect anomalies, we need to compare the current transaction amount against the median transaction amount of the last W minutes (a sliding time window).

However, the transaction volume is massive (millions per second). We need a data structure that allows us to:

Add a new transaction (with timestamp).

Remove old transactions (that fall out of the W minute window).

Query the current median efficiently.

Constraints:

Window size W can contain up to 10
5
  transactions.

Latency for Add, Remove, and GetMedian must be minimal (logarithmic or constant). O(N) is not allowed.

Example 1:
Window Size (W): 5 minutes.

Input Operations:

add(time=1, amount=10)
    Window: [10] Median: 10.0
add(time=2, amount=20)
    Window: [10, 20] Median: 15.0 (Average of 10, 20)
add(time=3, amount=30)
    Window: [10, 20, 30] Median: 20.0
add(time=7, amount=5)
    Current Time: 7. Window Range: [2, 7] (Time 7 - 5 = 2).
    Expired: Transaction at time=1 (Amount 10) is removed.
    Window: [20, 30, 5] --> Sorted: [5, 20, 30].
    Median: 20.0
'''
import heapq
from collections import defaultdict, deque


class FraudDetector:
    def __init__(self, window_size):
        self.window_size = window_size
        self.small = []  # Max-Heap (stores negative values)
        self.large = []  # Min-Heap
        self.debt = defaultdict(int)  # Tracks elements to be deleted
        self.queue = deque()  # Tracks timestamp order
        self.balance = 0  # Balance factor: len(small) - len(large) (considering valid items)

    def add_transaction(self, amount):
        # 1. Add to Queue
        self.queue.append(amount)

        # 2. Add to Heaps
        # Logic: Always push to small, then balance
        heapq.heappush(self.small, -amount)
        self.balance += 1

        # Ensure max(small) <= min(large)
        if self.small and self.large and (-self.small[0] > self.large[0]):
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
            self.balance -= 2  # Moved from small (+1) to large (-1), net change -2?
            # No. Balance tracks small - large.
            # Push small (+1). Move small->large (-1 small, +1 large) -> net -2 change to balance. Correct.

        # 3. Rebalance Sizes (0 <= balance <= 1)
        if self.balance > 1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
            self.balance -= 2
        elif self.balance < 0:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)
            self.balance += 2

        # 4. Remove Expired (Lazy)
        if len(self.queue) > self.window_size:
            expired = self.queue.popleft()
            self.debt[expired] += 1
            # Update balance based on where the expired element *likely* is
            # Ideally we check logic: if expired <= median, it's in small. Else large.
            # But simpler: balance is managed by valid counts.
            if expired <= -self.small[0]:
                self.balance -= 1  # Removing from small
            else:
                self.balance += 1  # Removing from large (so small - large increases relative)

            # Prune Dead elements from tops
            self._prune(self.small, -1)  # -1 multiplier for max heap
            self._prune(self.large, 1)

            # Rebalance again after logical removal
            if self.balance > 1:
                heapq.heappush(self.large, -heapq.heappop(self.small))
                self.balance -= 2
            elif self.balance < 0:
                heapq.heappush(self.small, -heapq.heappop(self.large))
                self.balance += 2

            self._prune(self.small, -1)
            self._prune(self.large, 1)

    def _prune(self, heap, multiplier):
        # While top of heap is in debt, pop it
        while heap and self.debt[multiplier * heap[0]] > 0:
            val = multiplier * heapq.heappop(heap)
            self.debt[val] -= 1

    def get_median(self):
        # Ensure tops are valid before peeking
        self._prune(self.small, -1)
        self._prune(self.large, 1)

        if self.balance == 1:
            return -self.small[0]
        else:
            return (-self.small[0] + self.large[0]) / 2.0


if __name__ == "__main__":

    print("--- Test 1: Basic Window (Size 3) ---")
    detector = FraudDetector(window_size=3)

    # Add 10: Window [10] -> Median 10
    detector.add_transaction(10)
    print(f"Added 10. Median: {detector.get_median()} (Expected: 10.0)")

    # Add 20: Window [10, 20] -> Median 15
    detector.add_transaction(20)
    print(f"Added 20. Median: {detector.get_median()} (Expected: 15.0)")

    # Add 30: Window [10, 20, 30] -> Median 20
    detector.add_transaction(30)
    print(f"Added 30. Median: {detector.get_median()} (Expected: 20.0)")

    # Add 40: Window Slides -> [20, 30, 40]. Median 30.
    # 10 is removed (Lazy removal).
    detector.add_transaction(40)
    print(f"Added 40. Window [20, 30, 40]. Median: {detector.get_median()} (Expected: 30.0)")

    print("\n--- Test 2: Odd/Even Transitions & Rebalancing ---")
    # Reset
    detector = FraudDetector(window_size=4)
    txns = [1, 2, 3, 4]
    for t in txns:
        detector.add_transaction(t)
    # Window: [1, 2, 3, 4]. Sorted: 1, 2, 3, 4. Median: (2+3)/2 = 2.5
    print(f"Window [1, 2, 3, 4]. Median: {detector.get_median()} (Expected: 2.5)")

    # Add 5. Window [2, 3, 4, 5]. Median (3+4)/2 = 3.5
    detector.add_transaction(5)
    print(f"Added 5. Window [2, 3, 4, 5]. Median: {detector.get_median()} (Expected: 3.5)")

    print("\n--- Test 3: Unsorted Input & Large Window ---")
    detector = FraudDetector(window_size=5)
    # Input: 5, 2, 8, 1, 9
    inputs = [5, 2, 8, 1, 9]
    for x in inputs:
        detector.add_transaction(x)

    # Sorted Window: 1, 2, 5, 8, 9. Median should be 5.
    print(f"Window {inputs}. Median: {detector.get_median()} (Expected: 5.0)")

    # Add 100. Window: [2, 8, 1, 9, 100]. Sorted: 1, 2, 8, 9, 100. Median 8.
    detector.add_transaction(100)
    print(f"Added 100 (Remove 5). Median: {detector.get_median()} (Expected: 8.0)")

    print("\n--- Test 4: Duplicate Values ---")
    # Handling duplicates is tricky for Lazy Removal if not implemented correctly
    detector = FraudDetector(window_size=3)
    detector.add_transaction(5)
    detector.add_transaction(5)
    detector.add_transaction(5)
    # Window [5, 5, 5]
    print(f"Window [5, 5, 5]. Median: {detector.get_median()} (Expected: 5.0)")

    # Add 10. Remove one 5. Window [5, 5, 10]. Median 5.
    detector.add_transaction(10)
    print(f"Added 10. Window [5, 5, 10]. Median: {detector.get_median()} (Expected: 5.0)")

    # Add 20. Remove another 5. Window [5, 10, 20]. Median 10.
    detector.add_transaction(20)
    print(f"Added 20. Window [5, 10, 20]. Median: {detector.get_median()} (Expected: 10.0)")