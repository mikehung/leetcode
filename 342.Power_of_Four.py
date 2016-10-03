#!/usr/bin/env python

class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        return not num&num-1 and bool(num&0x55555555)

for i in range(20):
	print(4**i,Solution().isPowerOfFour(4**i))
