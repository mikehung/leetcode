#!/usr/bin/env python3

import collections

class Solution(object):
    def knightProbability(self, N, K, r, c):
        """
        :type N: int (board)
        :type K: int (step)
        :type r: int
        :type c: int
        :rtype: float
        """
        moves = [(m[0]*s0, m[1]*s1) for m in [(1, 2), (2, 1)] for s0 in (1, -1) for s1 in (1, -1)]
        steps = collections.defaultdict(list)

        for i in range(N):
            for j in range(N):
                for move in moves:
                    next_pos = (i + move[0], j + move[1])
                    if (0, 0) <= next_pos < (N, N):
                        steps[(i, j)].append(next_pos)

        position = collections.defaultdict(int)
        position[(r, c)] = 1
        for _ in range(K):
            next_position = collections.defaultdict(int)
            for pos, count in position.items():
                for next_pos in steps[pos]:
                    next_position[next_pos] += position[pos]
            position = next_position

        return float(sum(position.values()))/(8**K)


def test(N, K, r, c):
    print(Solution().knightProbability(N, K, r, c))


test(3, 2, 0, 0)
test(3, 2, 1, 1)
test(25, 99, 1, 1)
test(25, 0, 1, 1)
