#!/usr/bin/env python

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        nums[:k], nums[k:] = nums[len(nums)-k:], nums[:len(nums)-k]
        print(nums)


a = Solution().rotate
a([],1)
a([1],1)
a([1],2)
a([1],3)
a([1,2,3], 0)
a([1,2,3], 1)
a([1,2,3], 2)
a([1,2,3], 3)
a([1,2,3], 4)
a([1,2,3,4,5,6,7], 3)
a([1,2,3,4,5,6], 2)
