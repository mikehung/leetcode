#!/usr/bin/env python

class Solution(object):
    def isSameTreeIterative(self, p, q):
        root_p, root_q = p, q
        stack = []

        while stack or root_p or root_q:
            if not root_p and not root_q:
                root_p, root_q = stack.pop()
                root_p, root_q = root_p.right, root_q.right
            elif not root_p or not root_q or root_p.val != root_q.val:
                return False
            else:
                stack.append((root_p, root_q))
                root_p, root_q = root_p.left, root_q.left
        return True

    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p and not q: return True
        if not p or not q: return False
        if p.val != q.val: return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
