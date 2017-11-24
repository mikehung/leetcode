#!/usr/bin/env python
# Time: O(n**2), n = len(s)
# Space: O(n**2)

# Errors:
#  v1: use dp but get TLE for s='d'*1000
#   => change to use memoization

class Solution(object):
    def find(self, s, dp, i, j):
        if i > j:
            return ''
        elif i == j:
            return s[i]
        elif i == j - 1:
            return s[i:j+1] if s[i] == s[j] else s[i]
        else:
            if s[i] == s[j]:
                return s[i] + self.find(s, dp, i+1, j-1) + s[j]
            else:
                if dp[i+1][j] > dp[i][j-1]:
                    return self.find(s, dp, i+1, j)
                else:
                    return self.find(s, dp, i, j-1)

    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        def count(i, j):
            if i > j:
                return 0
            if i == j:
                return 1
            key = (i-1) * len(s) + j
            if self.memo[key] != 0:
                return self.memo[key]
            if s[i] == s[j]:
                value = count(i+1, j-1) + 2
            else:
                value = max(count(i+1, j), count(i, j-1))
            self.memo[key] = value
            return value

        self.memo = [0] * (len(s)**2)
        return count(0, len(s)-1)


    def longestPalindromeSubseq_v1(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp = [[0 for c in range(len(s))] for r in range(len(s))]

        for i in range(len(s)):
            dp[i][i] = 1
        for i in range(len(s)-1):
            j = i + 1
            dp[i][j] = 2 if s[i] == s[j] else 1

        for d in range(2, len(s)):
            for i in range(len(s)-d):
                j = i + d
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])

        # print(self.find(s, dp, 0, len(s)-1))
        return dp[0][-1]


def test(s, e):
    r = Solution().longestPalindromeSubseq_v1(s)
    print(e == r, s, e, r)


test("bbbab", 4)
test("cbbd", 2)
test("aaccbbdesaabbccs", 10)
import time
beg = time.time()
s='d'*1000
test(s, 1000)
print(time.time() - beg)
