#!/usr/bin/env python

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def validBSTRange(root, low, high):
            if not root:
                return True
            if root.val <= low or root.val >= high:
                return False
            return validBSTRange(root.left, low, root.val) and validBSTRange(root.right, root.val, high)
        return validBSTRange(root, float('-inf'), float('inf'))
