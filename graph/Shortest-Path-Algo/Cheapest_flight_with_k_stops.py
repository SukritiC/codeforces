from collections import deque
class Solution:
    def CheapestFlight(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        adj = [[] for _ in range(n)]

        for it in flights:
            adj[it[0]].append((it[1],it[2]))

        minDist = [float('inf')] *n
        minDist[src] = 0

        q = deque([(0, src, 0)])

        while q:
            stop, node, dist = q.popleft()

            if stop > K:
                continue
            for adjNode, edge in adj[node]:
                if (dist + edge)< minDist[adjNode] and stop <= K:
                    minDist[adjNode] = dist+edge
                    q.append((stop+1, adjNode, dist+edge))

        if minDist[dst] == float('inf'):
            return -1
        return minDist[dst]