#!/usr/bin/env python

class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        count_prev = count_now = result = 0
        c_now = None

        for c in s:
            if c_now is None:
                count_now = 1
                c_now = c
                continue
            if c_now == c:
                count_now += 1
            else:
                if count_prev != 0:
                    result += min(count_prev, count_now)
                c_now = c
                count_prev = count_now
                count_now = 1

        if count_prev != 0:
            result += min(count_prev, count_now)

        return result


def test(s, e):
    r = Solution().countBinarySubstrings(s)
    print(e == r, s, e, r)

test("000", 0)
test("00110011", 6)
test("10101", 4)
test("00110", 3)
test("00100", 2)
