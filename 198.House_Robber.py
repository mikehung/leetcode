#!/usr/bin/env python

class Solution(object):
    def cal(self, nums, i, j):
        if not nums or i >= len(nums) or j >= len(nums) or i > j:
            return 0

        if self.dp[i][j] != -1:
            return self.dp[i][j]

        if i == j:
            val = nums[i]
        else:
            val = max(nums[i] + self.cal(nums, i+2, j), self.cal(nums, i+1, j))

        self.dp[i][j] = val
        return self.dp[i][j]

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

        r = self.cal(nums)
        print(max(r))
        return max(r)

# Solution().rob([1,2,3])

Solution().rob([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
