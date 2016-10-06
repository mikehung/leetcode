#!/usr/bin/env python

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left = '([{'
        right = ')]}'
        stack = []
        for c in s:
            if c in left:
                stack += [c]
            elif c in right:
                if not stack or right.index(c) != left.index(stack.pop()):
                    return False
            else:
                return False
        return not stack
