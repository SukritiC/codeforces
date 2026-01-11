'''
Scenario:
You are working on a Disaster Relief Logistics System. We have a network of N cities (labeled 0 to N-1) 
connected by roads. Each road has a travel time (weight).We have established K supply hubs at specific cities.
When a disaster strikes a city, we need to send relief supplies from the nearest supply hub to that city.However,
the road network is damaged. Some roads have a reliability score (probability of not collapsing).

We want to find a path from any supply hub to the disaster city such that:The path has the minimum possible travel time.
Among paths with the minimum travel time, we choose the one with the maximum reliability (product of
probabilities along the path). Or, if reliability is simple "safe/unsafe," let's stick to the product.

Correction: To keep it standard SDE 3: Assume roads are either Safe or Unsafe. We prefer Safe roads.Primary

Objective: Minimize Travel Time.Secondary Objective: Minimize the number of Unsafe roads used on that shortest path.

Input:
n: Number of cities.
roads: List of [u, v, time, is_safe] (where is_safe is 1 for safe, 0 for unsafe).
Undirected.hubs: Array of city indices [h1, h2, ..., hk].
dest: The disaster city index.

Output:Return an array [min_time, min_unsafe_count].If unreachable, return [-1, -1].

Constraints:N <= 10^5, E <= 2*10^5.Time limit is strict.

Example 1:
cities : 5
hubs: [0, 4]
dest: 3
roads :[
        [0, 1, 10, 1],
        [1, 3, 10, 1],
        [4, 2, 5, 0],
        [2, 3, 5, 1],
        ]

Output : [10, 1]

Example 2:

Cities: 3
Hubs: [0, 2]
Dest: 1
Roads:[
        [0, 1, 10, 0],
        [2, 1, 10, 1],
        ]


Result: [10, 0]
'''

import heapq


class Solution:
    def compute_min_time_route(self, cities, hubs, roads):
        adj = [[] for _ in range(cities)]
        for u, v, time, is_safe in roads:
            # Logic: If is_safe is 0 (Unsafe), cost is 1. If 1 (Safe), cost is 0.
            unsafe_cost = 1 if is_safe == 0 else 0
            adj[u].append((v, time, unsafe_cost))
            adj[v].append((u, time, unsafe_cost))

        # dist[i] = [min_time, min_unsafe_count]
        # Initialize time to infinity, unsafe count to infinity
        dist = [[float('inf'), float('inf')] for _ in range(cities)]
        pq = []

        # Multi-Source Initialization
        for hub in hubs:
            dist[hub] = [0, 0]
            # PQ stores: (time, unsafe_count, node)
            # Python's heap sorts by tuple elements in order: Time first, then Unsafe
            heapq.heappush(pq, (0, 0, hub))

        while pq:
            curr_time, curr_unsafe, u = heapq.heappop(pq)

            # Pruning: If we found a path that is strictly better (faster) OR
            # equal time but safer, ignore this one.
            # Note: We check strict dominance.
            if curr_time > dist[u][0] or (curr_time == dist[u][0] and curr_unsafe > dist[u][1]):
                continue

            for v, edge_time, edge_unsafe_cost in adj[u]:
                new_time = curr_time + edge_time
                new_unsafe = curr_unsafe + edge_unsafe_cost

                # Update Condition:
                # 1. Strictly faster time
                # 2. Same time, but fewer unsafe roads
                if new_time < dist[v][0] or (new_time == dist[v][0] and new_unsafe < dist[v][1]):
                    dist[v][0] = new_time
                    dist[v][1] = new_unsafe
                    heapq.heappush(pq, (new_time, new_unsafe, v))

        # Format output: if unreachable, return [-1, -1]
        result = []
        for d in dist:
            if d[0] == float('inf'):
                result.append([-1, -1])
            else:
                result.append(d)
        return result


if __name__ == "__main__":
    cities = 5
    hubs = [0, 4]
    dest = 3
    # [u, v, time, is_safe (1=Safe, 0=Unsafe)]
    roads = [
        [0, 1, 10, 1],  # Safe
        [1, 3, 10, 1],  # Safe -> Path 0->1->3: Time 20, Unsafe 0
        [4, 2, 5, 0],  # Unsafe (Cost 1)
        [2, 3, 5, 1],  # Safe -> Path 4->2->3: Time 10, Unsafe 1
    ]
    soln = Solution()
    ans = soln.compute_min_time_route(cities, hubs, roads)

    # Expected for dest 3: [10, 1] because 10 < 20 (Time is primary)
    print(f"Result for all cities: {ans}")
    print(f"Result for destination {dest}: {ans[dest]}")