class Solution:
    def maxMeetings(self, start, end):
        n = len(start)
        timings = []
        for i in range(n):
            timings.append([start[i], end[i]])

        timings.sort(key=lambda x: x[1])

        last_end_time = -1
        count = 0
        for pair in timings:
            if pair[0] > last_end_time:
                last_end_time = pair[1]
                count += 1

        return count




