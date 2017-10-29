#!/usr/bin/env python

class Solution(object):
    def minimumDeleteSum(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        dp = [[0 for i in range(len(s1)+1)] for j in range(len(s2)+1)]
        s1 = [ord(_) for _ in s1]
        s2 = [ord(_) for _ in s2]

        for i in range(1, len(s1)+1):
            dp[0][i] = s1[i-1]+dp[0][i-1]
        for j in range(1, len(s2)+1):
            dp[j][0] = s2[j-1]+dp[j-1][0]

        for i in range(1, len(s1)+1):
            for j in range(1, len(s2)+1):
                if s1[i-1] == s2[j-1]:
                    dp[j][i] = dp[j-1][i-1]
                else:
                    dp[j][i] = min(s1[i-1]+dp[j][i-1], s2[j-1]+dp[j-1][i])

        return dp[len(s2)][len(s1)]


print(Solution().minimumDeleteSum('sea', 'eat'))
print(Solution().minimumDeleteSum('delete', 'leet'))
