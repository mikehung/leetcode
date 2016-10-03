#!/usr/bin/env python

class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return bool(n) and not n&n-1

for i in range(20):
	print(i,Solution().isPowerOfFour(i))
