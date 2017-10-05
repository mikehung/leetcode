#!/usr/bin/env python3

from operator import add, sub, mul, truediv

class Solution(object):
    def judgePoint24(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) == 1 and abs(nums[0] - 24) <= 1e-9:
            return True

        for i1, n1 in enumerate(nums):
            for i2, n2 in enumerate(nums):
                if i1 == i2:
                    continue
                next_nums = [n for i, n in enumerate(nums) if i != i1 and i != i2]
                for op in (add, sub, mul, truediv):
                    if op == truediv and n2 == 0:
                        continue
                    if op in [add, mul] and i1 > i2:
                        continue
                    next_nums.append(op(n1, n2))
                    if (self.judgePoint24(next_nums)):
                        return True
                    next_nums.pop()

        return False


def test(nums, expect):
    result = Solution().judgePoint24(nums)
    print(result == expect, nums, expect, result)


test([6, 6, 6, 6], True)
test([4, 1, 8, 7], True)
test([1, 2, 1, 2], False)
test([8, 1, 3, 2], True)
test([3, 3, 8, 8], True)
