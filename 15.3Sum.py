#!/usr/bin/env python

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3: return []

        nums.sort()
        if nums[0] > 0 or nums[-1] < 0: return []
        result = []
        prev = None
        for k, v in enumerate(nums):
            if v == prev: continue
            prev = v
            i, j = 0, len(nums)-1
            while i < j:
                if i == k:
                    i += 1
                    continue
                elif j == k:
                    j -= 1
                    continue
                if nums[i] > 0 and nums[j] > 0 and nums[k] > 0:
                    break

                if nums[i] < 0 and nums[j] < 0 and nums[k] < 0:
                    break

                s = nums[i] + nums[j] + nums[k]
                if s == 0:
                    r = sorted([nums[i], nums[j], nums[k]])
                    if r not in result:
                        result.append(r)
                    i += 1
                    j -= 1
                elif s > 0:
                    j -= 1
                else:
                    i += 1

        return result
