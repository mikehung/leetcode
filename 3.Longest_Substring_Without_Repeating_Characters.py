#!/usr/bin/env python

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = 0
        substring = ''

        for c in s:
            if c not in substring:
                substring += c
            else:
                length = max(length, len(substring))
                substring = substring[substring.find(c) + 1:] + c

        return max(length, len(substring))

s = Solution().lengthOfLongestSubstring
s('abbbc')
s('')
s('abcabcbb')
s('pwwkew')
print(s("bpfbhmipx"))
s('aaaaaaa')
