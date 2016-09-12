#!/usr/bin/env python

class Solution(object):
    def cal(self, nums):
        if not nums:
            return (0, 0)

        cal_1 = self.cal(nums[1:])
        n = max(cal_1)
        y = nums[0] + cal_1[0]

        return (n, y)

    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        t = self.cal(nums[2:-1])
        r1 = nums[0] + max(t)
        r2 = max(self.cal(nums[1:]))

        print(max(r1, r2))
        return max(r1, r2)

# Solution().rob([1,2,3])
a = Solution().rob
a([2,1,1,1])
