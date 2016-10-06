#!/usr/bin/env python

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        prev = None
        result, diff = 0, float('inf')
        for k in range(len(nums)):
            if nums[k] == prev: continue
            prev = nums[k]

            i, j = 0, len(nums)-1
            while i < j:
                if i == k:
                    i += 1
                    continue
                elif j == k:
                    j -= 1
                    continue

                s = nums[i] + nums[j] + nums[k]
                if s == target:
                    return s

                if s < target:
                    i += 1
                else:
                    j -= 1

                if abs(target-s) < diff:
                    result, diff = s, abs(target-s)
        return result
