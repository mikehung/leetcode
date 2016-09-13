#!/usr/bin/env python
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        beg = 0
        end = len(nums) - 1

        while beg <= end:
            # find fisrt equal to val
            while beg < len(nums) and nums[beg] != val:
                beg += 1
            # find last not equal to val
            while end >= 0 and nums[end] == val:
                end -= 1
            if beg < end:
                nums[beg], nums[end] = nums[end], nums[beg]

        return end + 1

a = Solution().removeElement
a([], 0)
a([1], 1)
a([1,1,1], 1)
a([2,2,2], 1)
a([1,2,3], 1)
a([1,2,1], 1)
a([1,1,2,1,1,3], 1)
