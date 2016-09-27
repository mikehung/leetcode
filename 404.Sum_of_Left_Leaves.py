#!/usr/bin/env python

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def leave(root, left=True):
            if not root:
                return 0
            # leave
            if not root.left and not root.right:
                return root.val if left else 0
            return leave(root.left, True) + leave(root.right, False)
        return leave(root, True)
