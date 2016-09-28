#!/usr/bin/env python


class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        node = root
        stack, inorder = [], []
        while stack or node:
            if not node:
                node = stack.pop()
                inorder.append(node.val)
                node = node.right
            else:
                stack.append(node)
                node = node.left
        return inorder
