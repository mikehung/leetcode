#!/usr/bin/env python

import sys

class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq, first_index, last_index = dict(), dict(), dict()

        for index, num in enumerate(nums):
            if num not in freq:
                freq[num] = 1
                first_index[num] = last_index[num] = index
            else:
                freq[num] += 1
                last_index[num] = index

        degree = sys.maxint
        max_freq = max(freq.values())
        for num, f in freq.items():
            if f == max_freq:
                degree = min(degree, last_index[num]-first_index[num]+1)

        return degree

def test(nums, e):
    r = Solution().findShortestSubArray(nums)
    print(e == r, nums, e, r)

test([1, 2, 2, 3, 1], 2)
test([1,2,2,3,1,4,2], 6)
