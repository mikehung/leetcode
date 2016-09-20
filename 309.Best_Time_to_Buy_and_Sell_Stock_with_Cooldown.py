#!/usr/bin/env python

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        sell_at_1 = 0
        none_at_1 = float('-inf')
        buy_at_0 = float('-inf')
        none_at_0 = 0

        for price in prices:
            sell_at_1, none_at_1, buy_at_0, none_at_0 = \
                max(buy_at_0, none_at_1) + price,\
                max(none_at_1, buy_at_0),\
                none_at_0 - price,\
                max(none_at_0, sell_at_1)
            print([sell_at_1, none_at_1, buy_at_0, none_at_0])

        return max(sell_at_1, none_at_0)

s = Solution().maxProfit
s([])
s([1,1])
s([1,2,3,0,2])
