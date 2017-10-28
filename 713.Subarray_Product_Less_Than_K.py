#!/usr/bin/env python

import random
from time import time

class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        product = 1
        count = beg = end = 0
        while end < len(nums):
            product *= nums[end]
            while product >= k and beg <= end:
                product /= nums[beg]
                beg += 1
            count += end - beg + 1
            end += 1

        return count


def test(nums, k, e):
    beg = time()
    r = Solution().numSubarrayProductLessThanK(nums, k)
    print('Time cost: {}'.format(time()-beg))
    print(r == e, e, r)


test([10, 6, 5, 2], 100, 8)
random.seed(a=1)
array = [random.randrange(1, 1000) for _ in range(50000)]
test(array, 10000, 52906)
