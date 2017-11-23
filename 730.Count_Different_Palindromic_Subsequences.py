#!/usr/bin/env python
# Time: O(n**2), n = len(S)
# Space: O(n**2)

# Thinking:
#  1. use memoization to avoid computing the same subproblems
#  2. memo's data structure:
#      - dict[(l, r)]: too slow, we need to contruct tuple
#                      and use hashing with dict
#      - list(n**2): fast, we already know the memo size depends
#                    on the input string. index: (l-1)*len(S)+r

class Solution(object):
    def countPalindromicSubsequences_v2(self, S):
        M = 10**9 + 7
        len_S = len(S)

        # dp with string's length
        dp = [[0 for c in range(len_S)] for r in range(len_S)]
        for i in range(len_S):
            dp[i][i] = 1

        for length in range(1, len_S):
            for l in range(0, len_S-length):
                r = l+length
                if S[l] != S[r]:
                    dp[l][r] = dp[l+1][r]+dp[l][r-1]-dp[l+1][r-1]
                else:
                    i, j = l+1, r-1
                    while i <= r and S[i] != S[l]:
                        i += 1
                    while j >= l and S[j] != S[l]:
                        j -= 1
                    if i == r and j == l:
                        # there are no S[l] in S[l+1:r-1]
                        dp[l][r] = 2*dp[l+1][r-1] + 2
                    elif i == j:
                        # S[l+1:r-1] has only one S[l]
                        dp[l][r] = 2*dp[l+1][r-1] + 1
                    else:
                        # there are at least two S[l] in S[l+1:r-1]
                        dp[l][r] = 2*dp[l+1][r-1] - dp[i+1][j-1]

        return (dp[0][len_S-1] + M) % M


    def countPalindromicSubsequences(self, S):
        """
        :type S: str
        :rtype: int
        """
        def count(l, r):
            if l > r:
                return 0
            if r == l:
                return 1
            key = (l-1)*len_S+r
            if self.memo[key] is not None:
                return self.memo[key]
            if S[l] != S[r]:
                c = count(l+1, r) + count(l, r-1) - count(l+1, r-1)
            else:
                # i: the first S[l] index of S[l+1:r-1]
                # j: the last S[l] index of S[l+1:r-1]
                i, j = l+1, r-1
                while i <= r and S[i] != S[l]:
                    i += 1
                while j >= l and S[j] != S[l]:
                    j -= 1
                if i == r and j == l:
                    # there are no S[l] in S[l+1:r-1]
                    c = 2*count(l+1, r-1) + 2
                elif i == j:
                    # S[l+1:r-1] has only one S[l]
                    c = 2*count(l+1, r-1) + 1
                else:
                    # there are at least two S[l] in S[l+1:r-1]
                    c = 2*count(l+1, r-1) - count(i+1, j-1)
            self.memo[key] = c
            return c

        M = 10**9 + 7
        len_S = len(S)
        self.memo = [None]*(len_S**2)
        return (count(0, len_S-1) + M) % M


def test(S, e):
    s = Solution()
    r = s.countPalindromicSubsequences(S)
    r2 = s.countPalindromicSubsequences_v2(S)
    print(r == r2 == e, S, e, r, r2)


S='a'
e=1
test(S, e)
S='aa'
e=2
test(S, e)
S='ab'
e=2
test(S, e)
S='abccb'
e=7
test(S, e)
S='bccb'
e=6
test(S, e)
S='abcdabcdabcdabcdabcdabcdabcdabcddcbadcbadcbadcbadcbadcbadcbadcba'
e=104860361
test(S, e)
S='ababa'
e=9
test(S, e)
S='abacaba'
e=19
test(S, e)
S="daaaabaadcccbcbbaabdbccbbabccacdacdddacbadbadcadcb"
test(S, 99418)
import time
s = time.time()
S="dcabdacadbbabdabbacbdbadcacaadddabbdccadbaacdacacaadacccbadaccaddcccabccdcbdccdccaadbbcbcccbaadbccddcdbdbcbbadcdccbcabcddcdbcadcadaccacbdcccaacccbdccdcbbccbdbccbacabdbddaacccdccbaaadbbcdccdbddbbcbaacddbbacdbdcdacddbabdcdcbdcbbbcdcdaacbaacdacadacdcdcdcbdbbbaacccdddddddbbdadcaacaddbabbddccabacccaacbdddccaabbdcdccabadccbcdbdaccdcaadaccdbaaaababddddbdacdbdbaabbabcbbabbabcbadacdbccbbcccabaddddcbadbbadcabdbbddbbaacbdbbbbacdddbcdddbdbdcbcdadcccccdccddacddccbddbacababbbcbcadaddbdddcbddbaadacdbdabbabbbcdbdcccdadcbddbacccbacbcbcdccbadcaabdbacbdcddadcbddcadccddaddcdacdabbcbcdadbaacdadacacadbabcbdcabbdcbdbcbddbcddabbaaabadccdbccddcabddabcdbccaacbabacaccbbaccdcbcbdbcbdbccaddcadaaabcaaaaabcbdcadaacadbbbcdddbaabdcdabdbcacdcaaccdcbabadddddcaabbbacabdadcabdacddcdcadadbddccbabbabbcdbadcccacdcaaaadabcadaabcdaacadccdbbbacddabdadaabcbddcdabcaabbbdcccbcaaabaccbbcbbdbcadcdaadddacdbaccccdbcbbaccadacdbaccadabbbbcabcacabaaccbdcdbaddccdbdbdaacbdbcdadbdaddccbdddaadabdabadbacaabbbbabcdabbcbbddbcaadabadbbdacadadabd"
e=369668464
test(S, e)
print(time.time() -s)
