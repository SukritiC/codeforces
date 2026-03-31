"""
Given root of the binary tree, return its maximum depth.



A binary tree's maximum depth is number of nodes along the longest path from root node down to the farthest node.
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.data = val
#         self.left = left
#         self.right = right

class Solution:
    def countDepth(self, root, count):
        if root == None:
            return count
        left = self.countDepth(root.left, count + 1)
        right = self.countDepth(root.right, count + 1)
        return max(left, right)

    def maxDepth(self, root):
        return self.countDepth(root, 0)
