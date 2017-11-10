#!/usr/bin/env python
# Time: O(mn), m = len(A)+1, n = len(B)+1
# Space: O(min(m, n))

# findLength_1:
# Time: O(mn), m = len(A)+1, n = len(B)+1
# Space: O(mn)


class Solution(object):
    def findLength(self, A, B):
        if len(A) > len(B):
            A, B = B, A
        dp = [0 for _ in range(len(A)+1)]
        best = 0
        for bi in range(1, len(B)+1):
            for ai in range(len(A), 0, -1):
                if A[ai-1] == B[bi-1]:
                    dp[ai] = dp[ai-1] + 1
                    if dp[ai] > best:
                        best = dp[ai]
                else:
                    dp[ai] = 0
        return best


    def findLength_1(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        dp = [[0 for ai in range(len(A)+1)] for bi in range(len(B)+1)]
        for ai in range(1, len(A)+1):
            for bi in range(1, len(B)+1):
                if A[ai-1] == B[bi-1]:
                    dp[bi][ai] = dp[bi-1][ai-1] + 1
        return max([max(row) for row in dp])
