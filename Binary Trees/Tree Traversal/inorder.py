"""
Given root of binary tree, return the Inorder traversal of the binary tree.
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
        ans.append(root.data)
        self.function(root.right, ans)

    def inorder(self, root):
        ans = []
        self.function(root, ans)
        return ans