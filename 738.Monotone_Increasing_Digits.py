# generator cannot range
# div / float truediv //

class Solution:
    def monotoneIncreasingDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N < 10:
            return N

        digits = []
        while N:
            digits.append(N%10)
            N /= 10

        decrease = False
        result = []
        digits = list(reversed(digits))
        for i in range(len(digits)-1):
            if digits[i] <= digits[i+1]:
                result.append(digits[i])
            else:
                decrease = True
                break

        if not decrease:
            result.append(digits[-1])
        else:
            j = i - 1
            while j >= 0 and result[j] == digits[i]:
                j -= 1
            result = result[:j+1] + [digits[i]-1] + [9]*(len(digits)-j-2)

        n = 0
        for r in result:
            n = n*10 + r

        return n

print(Solution().monotoneIncreasingDigits(9))
print(Solution().monotoneIncreasingDigits(10))
print(Solution().monotoneIncreasingDigits(1234))
print(Solution().monotoneIncreasingDigits(1444))
print(Solution().monotoneIncreasingDigits(1443))
print(Solution().monotoneIncreasingDigits(14444443))
print(Solution().monotoneIncreasingDigits(1230))
print(Solution().monotoneIncreasingDigits(332))
