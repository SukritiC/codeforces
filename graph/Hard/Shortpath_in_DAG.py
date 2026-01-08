from collections import defaultdict
from typing import List


class Solution:
    def dfs(self, node, adj, vis, st):
        vis[node] = True
        for dest, wt in adj[node]:
            if not vis[dest]:
                self.dfs(dest, adj, vis, st)
        st.append(node)

    def shortestPath(self, N, M, edges):
        adj = defaultdict(list)
        for u, v, wt in edges:
            adj[u].append((v, wt))

        vis = [False] * N
        st = []

        for i in range(N):
            if not vis[i]:
                self.dfs(i, adj, vis, st)

        dist = [1e9] * N

        dist[0] = 0

        while st:
            ele = st.pop()
            for dest, wt in adj[ele]:
                dist[dest] = min(dist[dest], dist[ele] + wt)

        for i in range(N):
            if dist[i] == 1e9:
                dist[i] = -1

        return dist



