"""
Given root of binary tree, return the preorder traversal of the binary tree.
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.data= val
#         self.left = left
#         self.right = right

class Solution:
    def func(self, node, ans):
        if node is None:
            return

        ans.append(node.data)
        self.func(node.left, ans)
        self.func(node.right, ans)

    def preorder(self, root):
        ans = []
        self.func(root, ans)
        return ans