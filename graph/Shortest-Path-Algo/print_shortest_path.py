import heapq


class Solution:
    def shortestPath(self, n, m, edges):
        adj = [[] for _ in range(n + 1)]

        for edge in edges:
            adj[edge[0]].append((edge[1], edge[2]))
            adj[edge[1]].append((edge[0], edge[2]))
        pq = []
        parent = list(range(n + 1))
        dist = [float('inf')] * (n + 1)
        dist[1] = 0

        heapq.heappush(pq, (0, 1))
        while pq:
            dis, node = heapq.heappop(pq)

            for adjNode, edWt in adj[node]:

                if dis + edWt < dist[adjNode]:
                    dist[adjNode] = dis + edWt

                    heapq.heappush(pq, (dis + edWt, adjNode))

                    parent[adjNode] = node

        if dist[n] == float('inf'):
            return [-1]

        path = []

        node = n

        while parent[node] != node:
            path.append(node)
            node = parent[node]

        path.append(1)

        path.reverse()

        path.insert(0, dist[n])

        return path
