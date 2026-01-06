from collections import deque


class Solution:
    # Function to return the topological
    # sorting of given graph
    def topoSort(self, V, adj):

        # To store the result
        ans = []

        # To store the In-degrees of nodes
        inDegree = [0] * V

        # Calculating the In-degree of the given graph
        for i in range(V):
            for it in adj[i]:
                inDegree[it] += 1

        # Queue to facilitate BFS
        q = deque()

        # Add the nodes with no in-degree to queue
        for i in range(V):
            if inDegree[i] == 0:
                q.append(i)

        # Until the queue is empty
        while q:

            # Get the node
            node = q.popleft()

            # Add it to the answer
            ans.append(node)

            # Traverse the neighbours
            for it in adj[node]:

                # Decrement the in-degree
                inDegree[it] -= 1

                # Add the node to queue if
                # its in-degree becomes zero
                if inDegree[it] == 0:
                    q.append(it)

        # Return the result
        return ans


if __name__ == "__main__":

    V = 6
    adj = [
        [],
        [],
        [3],
        [1],
        [0, 1],
        [0, 2]
    ]

    # Creating an instance of
    # Solution class
    sol = Solution()

    # Function call to return the
    # topological sorting of given graph
    ans = sol.topoSort(V, adj)

    # Output
    print("The topological sorting of the given graph is:")
    for i in range(V):
        print(ans[i], end=" ")