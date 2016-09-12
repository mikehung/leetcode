#!/usr/bin/env python3

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def cal(self, root, idx):
        if not root:
            return 0

        if idx in self.dp:
            return self.dp[idx]

        c1 = []
        c2 = []

        if root.left:
            c1.append((root.left, idx*2+1))
        if root.right:
            c1.append((root.right, idx*2+2))
        for c, i in c1:
            if c.left:
                c2.append((c.left, i*2+1))
            if c.right:
                c2.append((c.right, i*2+2))

        v1 = root.val
        for c, i in c2:
            v1 += self.cal(c, i)
        v2 = 0
        for c, i in c1:
            v2 += self.cal(c, i)

        self.dp[idx] = max(v1, v2)
        return self.dp[idx]

    def rob_greedy(self, root):
        if not root:
            return (0, 0)

        r_result = self.rob_greedy(root.right)
        l_result = self.rob_greedy(root.left)

        not_rob = max(r_result) + max(l_result)
        rob = root.val + r_result[1] + l_result[1]
        return (not_rob, rob)

    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # self.dp = {}
        # return self.cal(root, 0)
        result = self.rob_greedy(root)
        return max(result[0], result[1])

Solution().rob(None)
