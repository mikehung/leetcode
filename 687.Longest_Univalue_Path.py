#!/usr/bin/env python

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def helper(node):
            if node is None:
                return 0

            level, value = 0, 0
            if node.left is not None:
                left_level = helper(node.left)
                if node.val == node.left.val:
                    value += left_level + 1
                    level = left_level + 1

            if node.right is not None:
                right_level = helper(node.right)
                if node.val == node.right.val:
                    value += right_level + 1
                    level = max(level, right_level + 1)

            if value > self.max_value:
                self.max_value = value

            return level

        self.max_value = 0
        helper(root)
        return self.max_value

tree = TreeNode(5,
        left=TreeNode(4,
         left=TreeNode(1),
         right=TreeNode(1)),
        right=TreeNode(5,
         left=None,
         right=TreeNode(5)))

print(Solution().longestUnivaluePath(tree))

tree = TreeNode(1,
        left=TreeNode(4,
         left=TreeNode(4),
         right=TreeNode(4)),
        right=TreeNode(5,
         left=None,
         right=TreeNode(5)))

print(Solution().longestUnivaluePath(tree))
