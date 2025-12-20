class Solution:
    def dfs(self, i, N, adj, vis, path_vis):
        vis[i] = True
        path_vis[i] = True
        for element in adj[i]:
            if path_vis[element]:
                return True
            elif not vis[element]:
                if self.dfs(element, N, adj, vis, path_vis):
                    return True

        path_vis[i] = False
        return False

    def isCyclic(self, N, adj):
        vis = [False] * N
        path_vis = [False] * N
        for i in range(N):
            if not vis[i]:
                if self.dfs(i, N, adj, vis, path_vis):
                    return True
        return False