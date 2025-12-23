class Solution:
    def insertNewInterval(self, Intervals, newInterval):
        result = []

        i = 0
        n = len(Intervals)

        while i < n and Intervals[i][1] < newInterval[0]:
            result.append(Intervals[i])
            i += 1

        while i < n and Intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(Intervals[i][0], newInterval[0])
            newInterval[1] = max(Intervals[i][1], newInterval[1])
            i += 1

        result.append(newInterval)

        while i < n:
            result.append(Intervals[i])
            i += 1
        return result


