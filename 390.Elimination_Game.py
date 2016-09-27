#!/usr/bin/env python

class Solution(object):
    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """
        start, size, direction = 1, 1, 1
        while n // 2:
            if direction or n % 2:
                start += size
            n, size, direction = n//2, size*2, direction^1
        return start

print(Solution().lastRemaining(1))
print(Solution().lastRemaining(2))
print(Solution().lastRemaining(3))
print(Solution().lastRemaining(10000000))
