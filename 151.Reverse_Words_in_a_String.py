#!/usr/bin/env python

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return ' '.join([_[::-1] for _ in s[::-1].split(' ') if _])

print(Solution().reverseWords('hi!'))
print(Solution().reverseWords('       I   am   Happy        '))
