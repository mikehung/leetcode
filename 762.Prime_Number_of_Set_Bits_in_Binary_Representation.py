class Solution:
    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """
        def is_prime(n):
            if n == 1:
                return False
            if n in prime:
                return prime[n]
            for i in range(2, int(n**0.5)+1):
                if n % i == 0:
                    prime[n] = False
                    return prime[n]
            prime[n] = True
            return prime[n]

        ans = 0
        prime = {}
        for num in range(L, R+1):
            set_bits = bin(num).count('1')
            if is_prime(set_bits):
                ans += 1
        return ans


L, R = 6 ,10
print(Solution().countPrimeSetBits(L, R))
L, R = 10, 15
print(Solution().countPrimeSetBits(L, R))
L, R = 842, 888
print(Solution().countPrimeSetBits(L, R))
