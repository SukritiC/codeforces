from collections import deque
def bfs(self, node, adj, vis, ans):
    q = deque()
    q.append(node)
    while q:
        node = q.popleft()
        ans.append(node)
        for i in adj[node]:
            if not vis[i]:
                vis[i] = 1
                q.append(i)


def bfsOfGraph(self, V, adj):
    vis = [0] * V
    ans = []
    for i in range(V):
        if vis[i] == 0:
            vis[i] = 1
            self.bfs(i, adj, vis, ans)

    return ans