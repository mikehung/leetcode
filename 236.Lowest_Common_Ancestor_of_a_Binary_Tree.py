# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        def findpath(root, node, path):
            if not root:
                return False
            path.append(root)
            if root == node:
                return True
            if findpath(root.right, node, path) or findpath(root.left, node, path):
                return True
            path.pop()
            return False

        path_p, path_q = [], []
        if not findpath(root, p, path_p) or not findpath(root, q, path_q):
            return None
        i = 0
        len_p, len_q = len(path_p), len(path_q)
        while i < len_p and i < len_q and path_p[i] == path_q[i]:
            i += 1
        return path_p[i-1]


def test(root, p, q, ans):
    ret = Solution().lowestCommonAncestor(root, p, q)
    ans_val = ans.val if ans else None
    ret_val = ret.val if ret else None
    print(ret == ans, ans_val, ret_val)


nodes = [TreeNode(i) for i in range(8)]
root = nodes[0]
nodes[0].left, nodes[0].right = nodes[1], nodes[2]
nodes[1].left, nodes[1].right = nodes[3], nodes[4]
nodes[2].left, nodes[2].right = nodes[5], nodes[6]

test(root, nodes[0], nodes[0], nodes[0])
test(root, nodes[7], nodes[0], None)
test(root, nodes[1], nodes[3], nodes[1])
test(root, nodes[1], nodes[5], nodes[0])
test(root, nodes[6], nodes[5], nodes[2])
