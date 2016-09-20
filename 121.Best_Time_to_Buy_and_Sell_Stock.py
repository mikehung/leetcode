#!/usr/bin/env python

import sys

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy = sys.maxint
        diff = 0

        for price in prices:
            if price < buy:
                buy = price
            else:
                diff = max(diff, price - buy)

        print(diff)
        return diff

s = Solution().maxProfit
s([])
s([1])
s([1,1,1,1])
s([7, 1, 5, 3, 6, 4])
s([7, 1, 5, 3, 6, 4, 1, 0, 7])
s([7,6,5,4,3,2,1])
