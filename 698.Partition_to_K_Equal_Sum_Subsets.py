#!/usr/bin/env python

class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        def canPartition(nums, visited, vn, si, cv, tv, k):
            if k == 1:
                return True
            if cv == tv:
                return canPartition(nums, visited, vn, 0, 0, tv, k-1)
            if cv > tv or vn < k:
                return False
            for i, n in enumerate(nums):
                if not visited[i]:
                    visited[i] = True
                    if canPartition(nums, visited, vn-1, i+1, cv+nums[i], tv, k):
                        return True
                    visited[i] = False
            return False

        length = sum(nums)
        if length % k != 0:
            return False

        tv = length / k
        if any([num > tv for num in nums]):
            return False

        visited = [False for _ in range(len(nums))]
        return canPartition(sorted(nums, reverse=True), visited, length, 0, 0, tv, k)


def test(nums, k, e):
    r = Solution().canPartitionKSubsets(nums, k)
    print(e == r, nums, k, e, r)


test([2,2,2,2,2,8,8,8,8,8], 5, True)
test([4, 3, 2, 3, 5, 2, 1], 4, True)
test([4, 3, 2, 3, 5, 2, 1], 10, False)
test([5,2,5,5,5,5,5,5,5,5,5,5,5,5,5,3], 15, True)
test([3522,181,521,515,304,123,2512,312,922,407,146,1932,4037,2646,3871,269], 5, True)
test([85,35,40,64,86,45,63,16,5364,110,5653,97,95], 7, False)
