#!/usr/bin/env python

class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def oneliner(self, root):
        return [str(root.val) + '->' + p for p in self.binaryTreePaths(root.left) + self.binaryTreePaths(root.right)] or [str(root.val)] if root else []

    def binaryTreePaths(self, root):
        if not root: return []
        if not root.left and not root.right: return [str(root.val)]
        path = []
        for child in (root.left, root.right):
            for p in self.binaryTreePaths(child):
                path.append(str(root.val) + '->' + p)
        return path
