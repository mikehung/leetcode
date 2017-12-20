class Solution:
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        dp = [0 for _ in range(len(cost))]

        for i, c in enumerate(cost):
            if i < 2:
                dp[i] = c
            else:
                dp[i] = min(dp[i-1], dp[i-2]) + c

        return min(dp[-2], dp[-1])


print(Solution().minCostClimbingStairs([10,15,20]))
cost=[1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
print(Solution().minCostClimbingStairs(cost))
