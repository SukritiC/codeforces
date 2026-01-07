class Solution:
    def dfs(self, i, adj, vis, st):
        vis[i] = 1
        for element in adj[i]:
            if vis[element] == 0:
                self.dfs(element, adj, vis, st)

        st.append(i)

    def topoSort(self, V, adj):
        ans = []
        st = []
        vis = [0] * V
        for i in range(V):
            if vis[i] == 0:
                self.dfs(i, adj, vis, st)

        while st:
            ans.append(st.pop())
        return ans

