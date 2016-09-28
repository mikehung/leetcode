#!/usr/bin/env python

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root: return []
        if not root.left and not root.right and root.val == sum: return [[root.val]]
        path = []
        for p in self.pathSum(root.left, sum-root.val) + self.pathSum(root.right, sum-root.val):
            path.append([root.val] + p)
        return path
