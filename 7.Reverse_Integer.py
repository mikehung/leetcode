#!/usr/bin/env python

import math

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        n = int(str(abs(x))[::-1])
        if n > 0x7fffffff:
            return 0
        return n if x >= 0 else -n

for i in xrange(-100, 100):
    print([i, Solution().reverse(i)])
