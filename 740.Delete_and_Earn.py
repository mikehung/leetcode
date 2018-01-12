# exceed the recursion limit
import sys
sys.setrecursionlimit(10000)

class Solution(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def earn(idx):
            if idx >= 10001:
                return 0
            if memo[idx] is None:
                memo[idx] = max(points[idx] + earn(idx+2),
                                earn(idx+1))
            return memo[idx]

        memo = [None for _ in range(10001)]
        points = [0 for _ in range(10001)]
        for num in nums:
            points[num] += num

        return earn(0)

print(Solution().deleteAndEarn([3, 4, 2]), 6)
print(Solution().deleteAndEarn([2, 2, 3, 3, 3, 4]), 9)
import random
nums=[random.randrange(1, 10001) for _ in range(20000)]
print(Solution().deleteAndEarn(nums))
