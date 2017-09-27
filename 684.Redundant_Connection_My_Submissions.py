#!/usr/bin/env python


class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        tree = {_:_ for _ in range(1, 1001)}
        for u, v in edges:
            if tree[u] == tree[v]:
                return [u, v]

            x, y = tree[u], tree[v]
            for i in tree:
                if tree[i] == x:
                    tree[i] = y



def test(i, o):
    r = Solution().findRedundantConnection(i)
    print(r == o, i, o, r)


test([[1,2], [1,3], [2,3]], [2,3])
test([[1,2], [2,3], [3,4], [1,4], [1,5]], [1,4])
