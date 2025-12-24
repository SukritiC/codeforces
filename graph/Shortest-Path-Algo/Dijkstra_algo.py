import heapq

class Solution:
    def dijkstra(self, V, adj, S):
        pq = []

        dist = [int(1e9)] * V

        dist[S] = 0

        heapq.heappush(pq, (0, S))
        while pq:
            dis, node = heapq.heappop(pq)

            for adjNode, edgeWt in adj[node]:
                if dis + edgeWt < dist[adjNode]:
                    dist[adjNode] = dis + edgeWt
                    heapq.heappush(pq, (dist[adjNode], adjNode))
        return dist



