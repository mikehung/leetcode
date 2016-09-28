#!/usr/bin/env python

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        def findPath(root, target):
            if not root: return []
            if root == target: return [root]
            path = findPath(root.left, target) or findPath(root.right, target)
            return [root] + path if path else []

        path_p, path_q = findPath(root, p), findPath(root, q)
        for i in range(min(len(path_p), len(path_q))):
            if path_p[i] != path_q[i]:
                return path_p[i-1]
        return path_p[i]
