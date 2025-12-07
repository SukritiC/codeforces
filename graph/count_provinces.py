from collections import deque


class Solution:
    def bfs(self, node, adjLs, vis):
        vis[node] = 1
        q = deque()
        q.append(node)

        while q:
            i = q.popleft()
            for adj in adjLs[i]:
                if vis[adj] != 1:
                    vis[adj] = 1
                    q.append(adj)

    def numProvinces(self, edges):
        V = len(edges)
        adjLs = [[] for _ in range(V)]
        for i in range(V):
            for j in range(V):
                if edges[i][j] == 1 and i != j:
                    adjLs[i].append(j)
                    adjLs[j].append(i)

        vis = [0] * V
        count = 0
        for i in range(V):
            if not vis[i]:
                count += 1
                self.bfs(i, adjLs, vis)
        return count
