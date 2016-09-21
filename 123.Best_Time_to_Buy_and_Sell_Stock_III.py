#!/usr/bin/env python

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # remove duplicate adjacency entry
        i, j = 0, 1
        while j < len(prices):
            if prices[i] != prices[j]:
                i += 1
                prices[i] = prices[j]
            j += 1
        prices = prices[:i+1]

        if len(prices) < 2:
            return 0

        length = len(prices)
        max_profit_beg, max_profit_end = [0]*length, [0]*length
        max_price_beg = min_price_beg = prices[0]
        max_price_end = min_price_end = prices[-1]

        for i in range(1, length):
            if prices[i] < min_price_beg:
                min_price_beg = max_price_beg = prices[i]
                max_profit_beg[i] = max_profit_beg[i-1]
            else:
                max_price_beg = max(max_price_beg, prices[i])
                max_profit_beg[i] = max(max_profit_beg[i-1], max_price_beg - min_price_beg)

            j = length-i-1
            if prices[j] > max_price_end:
                min_price_end = max_price_end = prices[j]
                max_profit_end[i] = max_profit_end[j+1]
            else:
                min_price_end = min(min_price_end, prices[j])
                max_profit_end[i] = max(max_profit_end[j+1], max_price_end - min_price_end)

        p = 0
        for i in range(length):
            p = max(p, max_profit_beg[i] + max_profit_end[i])

        print(p)
        return p

s = Solution().maxProfit

s([])
s([1])
s([1]*3)
s([1,2,3,2,5,0,1])
s([1,1,1,1,2,3,2,2,3,3,2,2,5,0,1])
s([2,1,2,0,1])
