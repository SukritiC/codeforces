class Solution:
    def dfs(self, node, adj, vis, ans):
        vis[node] = 1
        ans.append(node)
        for i in adj[node]:
            if not vis[i]:
                self.dfs(i, adj, vis, ans)
    def dfsOfGraph(self, V, adj):
        vis = [0]*V
        ans = []
        for i in range(V):
            if vis[i] == 0:
                self.dfs(i, adj, vis, ans)
        return ans