#!/usr/bin/env python

import math

class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        min_length = int(math.ceil(len(B)/len(A))) or 1
        for length in range(min_length, min_length+2):
            print(A*length)
            if B in A * length:
                return length
        return -1

print(Solution().repeatedStringMatch('abcd', 'cdabcdabcdab'))
print(Solution().repeatedStringMatch('abcd', 'cdabcdabcda'))
print(Solution().repeatedStringMatch('abcd', 'cdabcdabcdb'))
print(Solution().repeatedStringMatch(A, B))
