#!/usr/bin/env python


class Solution(object):
    def preorderTraversalIterative(self, root):
        node, stack, preorder = root, [], []

        while stack or node:
            if not node:
                node = stack.pop()
                node = node.right
            else:
                preorder.append(node.val)
                stack.append(node)
                node = node.left
        return preorder

    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def helper(root):
            if not root: return
            self.preorder.append(root.val)
            helper(root.left)
            helper(root.right)

        self.preorder = []
        helper(root)
        return self.preorder
