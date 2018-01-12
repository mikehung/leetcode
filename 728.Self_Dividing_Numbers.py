#!/usr/bin/env python

class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        def check(num):
            now = num
            if now == 0:
                return False

            while now:
                now, mod = divmod(now, 10)
                if mod == 0 or num % mod != 0:
                    return False
            return True

        return [i for i in range(left, right+1) if check(i)]


print(Solution().selfDividingNumbers(0, 22))
