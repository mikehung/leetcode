#!/usr/bin/env python

import math

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            n = -int(str(x)[1:][::-1])
            return n if n >= -math.pow(2, 31) else 0
        else:
            n = int(str(x)[::-1])
            return n if n < math.pow(2, 31) else 0

for i in xrange(-100, 100):
    print([i, Solution().reverse(i)])
