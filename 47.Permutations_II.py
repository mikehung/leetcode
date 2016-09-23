#!/usr/bin/env python
class Solution(object):
    def iterative(self, nums):
        result = [[]]

        for num in nums:
            next_ret = []
            for r in result:
                for i in range((r+[num]).index(num)+1):
                    next_ret.append(r[:i] + [num] + r[i:])
            result = next_ret
        return result


    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 2:
            return [nums]

        ret = []
        s = set()
        for i in range(len(nums)):
            if nums[i] in s:
                continue
            s.add(nums[i])
            nums[0], nums[i] = nums[i], nums[0]
            sub_ret = self.permuteUnique(nums[1:])
            for sr in sub_ret:
                ret.append([nums[0]] + sr)

            nums[0], nums[i] = nums[i], nums[0]

        return ret

def s(num):
    print(Solution().iterative(num))

s([])
s([1])
s([1,2])
s([1,2,3])
s([1,4,1,4])
s([1,1,3])
s([3,3,3])
