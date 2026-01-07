class Solution:
    def topoSort(self, V, adj):
        ans = []
        inDegree = [0] * V

        for i in range(V):
            for it in adj[i]:
                inDegree[it] += 1

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

    def findOrder(self, N, arr):
        adj = [[] for _ in range(N)]
        for u, v in arr:
            adj[v].append(u)

        ans = self.topoSort(N, adj)

        if len(ans) < N:
            return []
        return ans

