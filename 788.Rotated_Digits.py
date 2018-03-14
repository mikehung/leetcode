class Solution:
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        def valid(i):
            has2568 = False
            for c in str(i):
                if c in ['2', '5', '6', '9']:
                    has2568 = True
                elif c in ['3', '4', '7']:
                    return False
            return has2568

        ans = 0
        for i in range(1, N+1):
            if valid(i):
                ans += 1
        return ans


print(Solution().rotatedDigits(2))
print(Solution().rotatedDigits(8))
print(Solution().rotatedDigits(100))
