#!/usr/bin/env python

import bisect
import itertools
import heapq


class Solution(object):
    # Time: O(n + klogn), n = len(matrix)
    #  n: to build heap
    #  klogn: to pop item k-1 times
    # Space: O(n)
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        pq = [(i, 0, row[0]) for i, row in enumerate(matrix)]
        heapq.heapify(pq)
        for _ in range(k-1):
            item = heapq.heappop(pq)
            if item[1] != len(matrix[0]):
                x, y = item[0], item[1]+1
                heapq.heappush(pq, (x, y, matrix[x][y]))

        return pq[0][2]


    # Time: O(logclogn), c = max(matrix) - min(matrix), n = len(matrix[0])
    # Space: O(1)
    def kthSmallest2(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        n = len(matrix)
        lo, hi = matrix[0][0], matrix[n-1][n-1]
        while lo < hi:
            # mid is the mid_k smallest number
            mid = (lo + hi) / 2
            mid_k = 0
            for row in matrix:
                mid_k += bisect.bisect(row, mid)
            if mid_k < k:
                lo = mid + 1
            else:
                hi = mid

        return lo


def test(matrix, k, e):
    r = Solution().kthSmallest(matrix, k)
    print(e == r, k, e, r)


matrix = [
    [ 1,  5,  9, 17],
    [10, 11, 13, 18],
    [12, 13, 15, 19],
    [13, 14, 20, 22],
]

ans = list(sorted(itertools.chain(*matrix)))

for i in range(len(matrix)**2):
    test(matrix, i+1, ans[i])
