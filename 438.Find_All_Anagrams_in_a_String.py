#!/usr/bin/env python
# Time: O(n), n = len(s)
# Space: O(m), m = len(p)

from collections import Counter

class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        ret = []
        counter_p = Counter(p)
        counter_s = Counter(s[:len(p)-1])

        for ei in range(len(p)-1, len(s)):
            si = ei - len(p) + 1
            counter_s[s[ei]] += 1
            if counter_p == counter_s:
                ret.append(si)
            counter_s[s[si]] -= 1
            if counter_s[s[si]] == 0:
                del counter_s[s[si]]

        return ret


def test(s, p, e):
    r = Solution().findAnagrams(s, p)
    print(r == e, s, p, e, r)


test("cbaebabacd", "abc", [0, 6])
test("abab", "ab", [0, 1, 2])
test("abab", "xxxxxxab", [])
