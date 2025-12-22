class Solution:
    def JobScheduling(self, Jobs):
        Jobs.sort(key=lambda x: -x[2])

        n = len(Jobs)

        max_d = -1
        for job in Jobs:
            max_d = max(max_d, job[1])

        hash = [-1] * (max_d + 1)

        count_profit, count = 0, 0
        for i in range(n):
            for j in range(Jobs[i][1] - 1, -1, -1):
                if hash[j] == -1:
                    count += 1
                    hash[j] = Jobs[i][0]
                    count_profit += Jobs[i][2]
                    break
        return [count, count_profit]
