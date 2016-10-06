#!/usr/bin/env python
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def helper(left, right):
            if left == right == 0:
                return [[]]
            result = []
            if left:
                result += [['('] + p for p in helper(left-1, right)]
            if left < right:
                result += [[')'] + p for p in helper(left, right-1)]
            return result

        result = []
        for p in helper(n, n):
            result += [''.join(p)]
        return result

sol = Solution().generateParenthesis
for n in range(0, 6):
    r = sol(n)
    print(n, len(r))
    print(r)
