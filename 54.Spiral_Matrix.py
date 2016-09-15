#!/usr/bin/env python


class Solution(object):
    def getPath(self, x, y, m, n, d):
        if m == 0 or n == 0:
            return []

        path = []
        d = (d+1) % 4

        if d == 0: # right
            for c in range(0, n):
                path.append(self.matrix[x][c+y])
            path += self.getPath(x+1, y, m-1, n, d)
        elif d == 1: # down
            for r in range(0, m):
                path.append(self.matrix[r+x][n+y-1])
            path += self.getPath(x, y, m, n-1, d)
        elif d == 2: # left
            for c in range(n-1, -1, -1):
                path.append(matrix[m+x-1][c+y])
            path += self.getPath(x, y, m-1, n, d)
        else: # up
            for r in range(m-1, -1, -1):
                path.append(self.matrix[r+x][y])
            path += self.getPath(x, y+1, m, n-1, d)

        return path

    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """

        if not matrix:
            return matrix

        self.matrix = matrix
        return self.getPath(0, 0, len(matrix), len(matrix[0]), -1)

sol = Solution().spiralOrder

matrix = [[]]
sol(matrix)

matrix = [
    [1,2,3],
    [8,9,4],
    [7,6,5]
]
sol(matrix)

matrix = [[1]]
sol(matrix)

matrix = [
    [1,2],
    [4,3],
]
sol(matrix)

matrix = [
    [ 1, 2, 3, 4, 5],
    [14,15,16,17, 6],
    [13,20,19,18, 7],
    [12,11,10, 9, 8]
]
sol(matrix)
