#!/usr/bin/env python


class Solution(object):
    def postorderTraversal(self, root):
        if not root: return []

        stack, order = [root], []
        prev = curr = None
        while stack:
            curr = stack[-1]
            # traverse down
            if not prev or prev.left == curr or prev.right == curr:
                if curr.left:
                    stack.append(curr.left)
                elif curr.right:
                    stack.append(curr.right)
            elif curr.left == prev:
                if curr.right:
                    stack.append(curr.right)
            else:
                order.append(curr.val)
                stack.pop()
            prev = curr
