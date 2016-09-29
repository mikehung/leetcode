#!/usr/bin/env python

import math

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        n, y = 0, abs(x)
        while y > 0:
            d, m = divmod(y, 10)
            n, y = n*10+m, d

        if n > 0x7fffffff:
            return 0
        return n if x >= 0 else -n

for i in xrange(-100, 100):
    print([i, Solution().reverse(i)])
i = 123456
print([i, Solution().reverse(i)])
i = -123456
print([i, Solution().reverse(i)])
