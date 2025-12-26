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

if __name__ == '__main__':
    V = 4
    adj = [[[1, 1], [3, 2]],[[0, 1], [2, 4]],[[1, 4], [3, 3]], [[0, 2], [2, 3]]]
    S = 0
    soln = Solution()
    print(soln.dijkstra(V, adj, S))


