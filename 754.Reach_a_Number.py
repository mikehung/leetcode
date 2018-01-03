class Solution:
    def reachNumber(self, target):
        """
        :type target: int
        :rtype: int
        """
        if target == 0:
            return 0
        if target < 0:
            target = -target

        s1 = s2 = n = 0
        while True:
            s1, s2 = s2, s2 + n
            if s1 <= target <= s2:
                break
            n += 1

        if target == s1:
            return n - 1
        elif target == s2:
            return n

        best = min(n-1+2*(target-s1), n+2*(s2-target))
        while True:
            if (s2 - target) % 2 == 0:
                diff = s2 - target
                if diff // 2 < n and n < best:
                    best = n
                break
            n += 1
            s2 += n

        return n


for i in range(30):
    print(i, Solution().reachNumber(i))
print(-1000000000, Solution().reachNumber(-1000000000))
