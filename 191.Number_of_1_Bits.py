#!/usr/bin/env python

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        return 0 if n == 0 else self.hammingWeight(n&n-1)+1

for i in xrange(10):
    print(str(i) + ' : ' + str(Solution().hammingWeight(i)))
