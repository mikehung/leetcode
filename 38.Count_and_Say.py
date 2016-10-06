#!/usr/bin/env python

class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        result = '1'
        for i in range(1,n):
            prev, count, l = result[0], 1, []
            for x in result[1:]:
                if x == prev:
                    count += 1
                else:
                    l += [str(count) + prev]
                    prev, count = x, 1
            l += [str(count) + prev]
            result = ''.join(l)

        return result

for i in range(1,10):
    print(Solution().countAndSay(i))
