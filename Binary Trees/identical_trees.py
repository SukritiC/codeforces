'''
Given the roots of two binary trees p and q, write a function to check if they are the same or not.



Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.data = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p, q):
        if p == None and q == None:
            return True
        if p == None or q == None:
            return False
        if p.data != q.data:
            return False

        left = self.isSameTree(p.left, q.left)
        right = self.isSameTree(p.right, q.right)

        return left and right