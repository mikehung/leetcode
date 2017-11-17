#!/usr/bin/env python
# Time: O(st), s = len(S), t = len(T)
# Space: O(s)

import sys


class Solution(object):
    def minimumWindowSubsequence(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        if not T:
            return ''

        row = [i if S[i] == T[0] else -1 for i in range(len(S))]
        for j in range(1, len(T)):
            start = -1
            nxt = [-1 for i in range(len(S))]
            for i in range(len(S)):
                if start != -1 and S[i] == T[j]:
                    nxt[i] = start
                if row[i] != -1:
                    start = row[i]
            row = nxt

        start, diff = -1, sys.maxint
        for i, v in enumerate(row):
            if v != -1 and i-v < diff:
                start, diff = v, i-v

        return '' if start == -1 else S[start:start+diff+1]


def test(S, T, e):
    r = Solution().minimumWindowSubsequence(S, T)
    print(e == r, S, T, e, r)


test('bcd', 'bcd', 'bcd')
test('bcde', 'bcd', 'bcd')
test('bcd', 'bcde', '')
test('aaaaa', 'aa', 'aa')
test('aaaaa', 'aba', '')
test('aaaaabbba', 'aba', 'abbba')
test('abcdebdde', 'bde', 'bcde')
test('abcdebddebde', 'bde', 'bde')
test('abcdebddebde', 'bxde', '')
test('', '', '')
test('aaaaabbba', 'aba', 'abbba')
