#!/usr/bin/env python
# Time: O(n), n = len(nums)
# Space: O(1)


class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ls, rs = 0, sum(nums)
        for idx, num in enumerate(nums):
            ls += num
            if ls == rs:
                return idx
            rs -= num

        return -1

def test(nums, e):
    r = Solution().pivotIndex(nums)
    print(e == r, nums, e, r)


test([1, 7, 3, 6, 5, 6], 3)
test([1, 2, 3], -1)
test([1, 1, 1, 1], -1)
test([1, 1, 1], 1)
test([1], 0)
