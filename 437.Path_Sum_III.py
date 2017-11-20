#!/usr/bin/env pyhon
# Time: O(n), n: number of nodes
# Space: O(h), h = tree's hight

from collections import defaultdict

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

class Solution(object):
    def pathSum(self, root, sum_):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        def check(node, prefix_sum, curr_sum):
            if not node:
                return 0

            curr_sum += node.val
            hit = prefix_sum[curr_sum-sum_]
            prefix_sum[curr_sum] += 1
            hit += check(node.left, prefix_sum, curr_sum)
            hit += check(node.right, prefix_sum, curr_sum)
            prefix_sum[curr_sum] -= 1

            return hit

        prefix_sum = defaultdict(int)
        prefix_sum[0] = 1
        return check(root, prefix_sum, 0)


def T(s):
    def v(x):
        return None if x is None else TreeNode(x)
    def c(l):
        if not l or not l[0]:
            return None
        root = TreeNode(l[0])
        nodes = [root]
        for i in range(1, len(l), 2):
            node = nodes.pop(0)

            node.left = v(l[i])
            if node.left:
                nodes.append(node.left)
            if i+1 == len(l):
                break
            node.right = v(l[i+1])
            if node.right:
                nodes.append(node.right)

        return root

    l = [None if _ == 'null' else int(_)  for _ in s[1:-1].split(',')]

    return c(l)


def P(root):
    def p(node):
        print(node.val if node else 'null')

    nodes = [root]
    while nodes:
        next_nodes = []
        print([n.val if n is not None else 'null' for n in nodes])
        for node in nodes:
            if node is not None:
                next_nodes.append(node.left)
                next_nodes.append(node.right)
        nodes = next_nodes


s='[1,0,1,1,2,0,-1,0,1,-1,0,-1,0,1,0]'
# P(T(s))
s='[1,0,1,1,2,0,-1,0,1,-1,0,-1,0,null,0]'
# P(T(s))
s='[1,1,1,1,1,1,1]'
print(Solution().pathSum(T(s), 3))
s='[10,5,-3,3,2,null,11,3,-2,null,1]'
print(Solution().pathSum(T(s), 8))
print(Solution().pathSum(T(s), 21))
s='[-3,3,3]'
print(Solution().pathSum(T(s), 0))
