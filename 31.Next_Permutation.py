#!/usr/bin/env python

class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # pos1: the biggest index of nums[pos1] < nums[pos1+1]
        # pos2: the lasted item of nums[pos1] < nums[pos2]
        pos1 = -1
        for i in range(len(nums)-1, 0, -1):
            if nums[i-1] < nums[i]:
                pos1 = i-1
                break

        if pos1 == -1:
            nums.sort()
            return

        pos2 = pos1+1
        for j in range(len(nums)-1, pos1, -1):
            if nums[j] > nums[pos1]:
                pos2 = j
                break

        # swap nums[pos1], nums[pos2] and then reverse nums[pos1+1:]
        nums[pos1], nums[pos2] = nums[pos2], nums[pos1]
        i = pos1 + 1
        j = len(nums) - 1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1

        return nums

def s(n):
    print(str(n) + ' -> ' + str(Solution().nextPermutation(n)))

s([])
s([1])
s([1,1])
s([1,2])
s([2,1])
s([1,2,3])
s([1,3,2])
s([2,1,3])
s([2,3,1])
s([3,1,2])
s([3,2,1])
s([5,1,1])
s([38,2,6,5,3,2])
