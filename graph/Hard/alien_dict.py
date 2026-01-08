from collections import deque


class Solution:
    def toposort(self, V, adj):
        inDegree = [0] * V
        for i in range(V):
            for it in adj[i]:
                inDegree[it] += 1

        ans = []
        q = deque()

        for i in range(V):
            if inDegree[i] == 0:
                q.append(i)

        while q:
            node = q.popleft()
            ans.append(node)

            for it in adj[node]:
                inDegree[it] -= 1
                if inDegree[it] == 0:
                    q.append(it)
        return ans

    def findOrder(self, dict, N, K):
        adj = [[] for _ in range(K)]

        for i in range(N - 1):
            s1 = dict[i]
            s2 = dict[i + 1]
            length = min(len(s1), len(s2))

            for ptr in range(length):
                if s1[ptr] != s2[ptr]:
                    adj[ord(s1[ptr]) - ord('a')].append(ord(s2[ptr]) - ord('a'))
                    break

        ans = self.toposort(K, adj)
        final_ans = ""

        for i in range(K):
            final_ans += chr(ord('a') + ans[i])
            final_ans += ' '
        return final_ans


