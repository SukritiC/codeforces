from collections import deque


class Solution:
    def bfs(self, i, adj, vis):
        q = deque()

        vis[i] = True
        q.append((i, -1))

        while q:
            curr, parent = q.popleft()
            for ele in adj[curr]:
                if not vis[ele]:
                    vis[ele] = True
                    q.append((ele, curr))
                elif ele != parent:
                    return True
        return False

    def isCycle(self, V, adj):
        vis = [False] * V
        ans = False

        for i in range(V):
            if not vis[i]:
                ans = self.bfs(i, adj, vis)

                if ans:
                    break
        return ans
