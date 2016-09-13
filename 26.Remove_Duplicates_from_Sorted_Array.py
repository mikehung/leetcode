#!/usr/bin/env python

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        i = 0
        for j in range(1, len(nums)):
            if nums[i] != nums[j]:
                nums[i+1] = nums[j]
                i += 1

        print(nums[:i+1])
        return i + 1

a = Solution().removeDuplicates
a([])
a([1,2,3])
a([1,1,3])
a([1,1,1])
a([1,1,3,3,3,4,5,5,5])
