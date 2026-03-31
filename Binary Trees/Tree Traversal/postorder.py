"""
Given root of binary tree, return the Postorder traversal of the binary tree.
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.data = val
#         self.left = left
#         self.right = right

class Solution:
    def function(self, root, ans):
        if root is None:
            return
        self.function(root.left, ans)
        self.function(root.right, ans)
        ans.append(root.data)

    def postorder(self, root):
        ans = []
        self.function(root, ans)
        return ans