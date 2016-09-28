#!/usr/bin/env python

class Solution(object):
    def isSymmetricIterative(self, root):
        if not root: return True
        stack = [(root.left, root.right)]
        while stack:
            next_stack = []
            for (left, right) in stack:
                if not left and not right: continue
                if not left or not right or left.val != right.val: return False
                next_stack.extend(((left.left, right.right), (left.right, right.left)))
            stack = next_stack
        return True

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def helper(left, right):
            if not left and not right: return True
            if not left or not right or left.val != right.val: return False
            return helper(left.left, right.right) and helper(left.right, right.left)

        if not root: return True
        return helper(root.left, root.right)
