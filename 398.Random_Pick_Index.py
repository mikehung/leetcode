#!/usr/bin/env python

import random

class Solution(object):

    def __init__(self, nums):
        """

        :type nums: List[int]
        :type numsSize: int
        """
        self.nums = nums
        random.seed()

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        index = -1
        count = 0
        for i in range(len(self.nums)):
            if self.nums[i] == target:
                count += 1
                if index == -1 or random.randrange(count) == 0:
                    index = i

        return index


# Your Solution object will be instantiated and called as such:
obj = Solution([1,2,3,3,3])
print(obj.pick(1))
for i in range(10):
    print(obj.pick(3))
