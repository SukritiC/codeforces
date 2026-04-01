"""
Given a binary tree root, find if it is height-balanced or not.

A tree is height-balanced if the difference between the heights of left and right subtrees is not more than one for all nodes of the tree.

"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def isBalanced(self, root):

        def dfsHeight(root):
            if not root:
                return 0

            leftHeight = dfsHeight(root.left)

            if leftHeight == -1:
                return -1

            rightHeight = dfsHeight(root.right)

            if rightHeight == -1:
                return -1

            if abs(leftHeight - rightHeight) > 1:
                return -1

            return max(leftHeight, rightHeight) + 1

        return dfsHeight(root) != -1
