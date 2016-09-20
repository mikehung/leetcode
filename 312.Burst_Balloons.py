#!/usr/bin/env python

class Solution(object):
    def p(self, nums, pos, i, j):
        if pos[i][j] == 0:
            return
        self.p(nums, pos, i, pos[i][j] - 1)
        self.p(nums, pos, pos[i][j] + 1, j)
        print(nums[pos[i][j]])

    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = [1] + nums + [1]
        length = len(nums)
        coin = [[0 for i in range(length)] for j in range(length)]
        pos = [[0 for i in range(length)] for j in range(length)]

        for l in range(1, length - 1):
            for i in range(1, length - l):
                j = i + l - 1
                for k in range(i, j + 1):
                    c = coin[i][k-1] + coin[k+1][j] + nums[i-1]*nums[j+1]*nums[k]
                    if c > coin[i][j]:
                        coin[i][j] = c
                        pos[i][j] = k
                    # coin[i][j] = max(coin[i][j], coin[i][k-1] + coin[k+1][j] + nums[i-1]*nums[j+1]*nums[k])

        print(coin)
        print(pos)
        self.p(nums, pos, 1, length - 2)
        return coin[1][length - 2]

s = Solution().maxCoins
s([3,1,5,8])
