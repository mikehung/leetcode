class Solution:
    def kthGrammar(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: int
        """
        flip = False
        while K > 2:
            if K % 2 == 0:
                flip = not flip
            K = (K+1)//2
        return [1, 0][K-1] if flip else [0, 1][K-1]

#01101001
i = 5
print(Solution().kthGrammar(4, i))
print(Solution().kthGrammar(4, i+1))
print(Solution().kthGrammar(4, i+2))
print(Solution().kthGrammar(4, i+3))
