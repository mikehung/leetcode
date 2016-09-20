#!/usr/bin/env python

import sys

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy = sys.maxint
        profit = 0
        diff = 0

        for price in prices:
            d = price - buy
            if d > 0:
                diff += d
            else:
                profit += diff
                diff = 0
            buy = price
        profit += diff

        return profit

s = Solution().maxProfit
s([])
s([1])
s([1,1,1])
s([1,2,3,1,2])
s([1,2,1,2])
