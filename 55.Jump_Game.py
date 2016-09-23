#!/usr/bin/env python

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        i, s = len(nums)-1, 0

        while i > 0:
            s += 1
            j = i-s
            if j < 0:
                break
            if nums[j] >= s:
                i, s = j, 0

        return i == 0

print(Solution().canJump([2,3,1,1,4]))
print(Solution().canJump([3,2,1,0,4]))
print(Solution().canJump([5,3,2,1,0,4]))
print(Solution().canJump([0,5,3,2,1,0,4]))
print(Solution().canJump([2,0,5,3,2,1,0,4]))
print(Solution().canJump([1,2,0,5,3,2,1,0,4]))
