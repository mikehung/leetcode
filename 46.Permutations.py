#!/usr/bin/env python
class Solution(object):
    def iterative(self, nums):
        result = [[]]

        for num in nums:
            next_ret = []
            for r in result:
                for i in range(len(r)+1):
                    next_ret.append(r[:i] + [num] + r[i:])
            result = next_ret
        return result


    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 2:
            return [nums]

        ret = []
        for i in range(len(nums)):
            nums[0], nums[i] = nums[i], nums[0]
            sub_ret = self.permute(nums[1:])
            for sr in sub_ret:
                ret.append([nums[0]] + sr)

            nums[0], nums[i] = nums[i], nums[0]

        return ret

def s(num):
    print(Solution().permute(num))

s([])
s([1])
s([1,2])
s([1,2,3])
s([1,2,3,4])
