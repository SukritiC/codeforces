"""
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).
"""
from collections import deque
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.data = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root):
        ans = []
        if not root:
            # If the tree is empty, return an empty list
            return ans

        # Create a queue to store nodes for level-order traversal
        q = deque([root])

        while q:
            # Create a list to store nodes at the current level
            level = []
            for _ in range(len(q)):
                # Get the front node from the queue
                node = q.popleft()
                # Add the node value to the current level list
                level.append(node.data)

                # Enqueue the child nodes if they exist
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            # Add the current level to the answer list
            ans.append(level)
        # Return the level-order traversal of the tree
        return ans