#!/usr/bin/env python

class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """

        if not n:
            return []

        matrix = [[0 for i in range(n)] for j in range(n)]

        num = 0
        u = l = 0
        d = r = n-1

        while True:
            for col in range(l, r+1):
                num += 1
                matrix[u][col] = num
            u += 1
            if u > d: break

            for row in range(u, d+1):
                num += 1
                matrix[row][r] = num
            r -= 1
            if r < l: break

            for col in range(r, l-1, -1):
                num += 1
                matrix[d][col] = num
            d -= 1
            if d < u: break

            for row in range(d, u-1, -1):
                num += 1
                matrix[row][l] = num
            l += 1
            if l > r: break

        print(matrix)
        return matrix

sol = Solution().generateMatrix

for i in range(0, 7):
    sol(i)
