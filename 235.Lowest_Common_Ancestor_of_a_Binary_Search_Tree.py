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
        def has(root, p):
            if not root:
                return False
            return root == p or has(root.left, p) or has(root.right, p)

        if not has(root, p) or not has(root, q):
            return None

        small_val = p.val if p.val < q.val else q.val
        big_val = q.val if p.val < q.val else p.val
        while True:
            if small_val > root.val:
                root = root.right
            elif big_val < root.val:
                root = root.left
            else:
                break
        return root


def test(root, p, q, ans):
    ret = Solution().lowestCommonAncestor(root, p, q)
    ans_val = ans.val if ans else None
    ret_val = ret.val if ret else None
    print(ret == ans, ans_val, ret_val)


nodes = [TreeNode(i) for i in [8, 5, 12, 1, 7, 9, 13, 15]]
root = nodes[0]
nodes[0].left, nodes[0].right = nodes[1], nodes[2]
nodes[1].left, nodes[1].right = nodes[3], nodes[4]
nodes[2].left, nodes[2].right = nodes[5], nodes[6]


test(root, nodes[0], nodes[0], nodes[0])
test(root, nodes[7], nodes[0], None)
test(root, nodes[1], nodes[3], nodes[1])
test(root, nodes[1], nodes[5], nodes[0])
test(root, nodes[6], nodes[5], nodes[2])
