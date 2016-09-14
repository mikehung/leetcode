#!/usr/bin/env python

class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            print(str(nums) + ': ' + str(len(nums)))
            return len(nums)

        diff = nums[1] - nums[0]
        if diff == 0:
            length = 1
        else:
            length = 2

        for i in range(2, len(nums)):
            if (nums[i] > nums[i - 1] and diff <= 0) or (nums[i] < nums[i - 1] and diff >= 0):
                length += 1
                diff = nums[i] - nums[i - 1]

        print(str(nums) + ': ' + str(length))
        return length

sol = Solution().wiggleMaxLength
sol([])
sol([1])
sol([1,2])
sol([3,2])
sol([3,3])
sol([1,2,3,4,5,6,7,8,9])
sol([1,7,4,9,2,5])
sol([1,17,5,10,13,15,10,5,16,8])
sol([2,4,5,7,5,5,7,1,2,3])
sol([3,3,3,2,5])
