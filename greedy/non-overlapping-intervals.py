class Solution:
    def MaximumNonOverlappingIntervals(self, Intervals):
        # your code goes here
        Intervals.sort(key=lambda x: x[1])

        count = 0
        last_end_time = -1
        for pair in Intervals:
            if pair[0] >= last_end_time:
                last_end_time = pair[1]
                count += 1

        return len(Intervals) - count