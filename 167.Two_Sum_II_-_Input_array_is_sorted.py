#!/usr/bin/env python
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        beg = 0
        end = len(numbers) - 1

        while True:
            result = numbers[beg] + numbers[end]
            if result == target:
                break
            elif result > target:
                end -= 1
            else:
                beg += 1

        return [beg + 1, end + 1]

sol = Solution().twoSum
sol([2,7,11,15,16], 2+7)
sol([2,7,11,15,16], 2+11)
sol([2,7,11,15,16], 2+15)
sol([2,7,11,15,16], 2+16)
sol([2,7,11,15,16], 7+11)
sol([2,7,11,15,16], 7+15)
sol([2,7,11,15,16], 7+16)
sol([2,7,11,15,16], 11+15)
sol([2,7,11,15,16], 11+16)
sol([2,7,11,15,16], 15+16)
