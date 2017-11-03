#!/usr/bin/env python
# Time: O(nlogn + nlogw), n = len(nums), w = max(nums)-min(nums)
# Space: O(1)

import bisect


class Solution(object):
    def smallestDistancePair(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        lo, hi = 0, nums[-1]-nums[0]
        while lo < hi:
            mid = (lo+hi)//2
            mid_k, left = 0, 0
            # use window sliding technique: O(n)
            # use bisect for every elements: O(nlogn)
            for right, n in enumerate(nums):
                while n-nums[left] > mid:
                    left += 1
                mid_k += right-left

            if mid_k < k:
                lo = mid+1
            else:
                hi = mid

        return lo

def test(nums, k, e):
    r = Solution().smallestDistancePair(nums, k)
    print(e == r, nums, k, e, r)


nums = [1, 5, 11, 20]
ans = [4, 6, 9, 10, 15, 19]

import time
b = time.time()
test(nums, 3, 9)
for i, i_n in enumerate(ans):
    test(nums, i+1, i_n)

nums = [9,10,7,10,6,1,5,4,9,8]
test(nums, 18, 2)
print('')
for i in range((len(nums)**2-len(nums))//2):
    test(nums, i+1, 0)
print(time.time()-b)
