class Solution:
    def numTilings(self, N):
        """
        :type N: int
        :rtype: int
        """
        dp = [0]*(N+1)
        dp[:3] = 1, 1, 2
        for i in range(3, N+1):
            dp[i] = dp[i-1]+dp[i-2]+2*(i-2)
        return dp[-1]

for i in range(1, 100):
    print(i, Solution().numTilings(i))
