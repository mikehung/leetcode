# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def findClosestLeaf(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        def getLevel(node):
            if not node:
                return float('inf'), None
            if not node.left and not node.right:
                # child
                level[node.val] = (0, node.val)
            else:
                ll, lv = getLevel(node.left)
                rl, rv = getLevel(node.right)
                l, v = (ll+1, lv) if ll < rl else (rl+1, rv)
                level[node.val] = (l, v)
            return level[node.val]

        def find(node):
            if not node:
                return None, None

            if node.val == k:
                ll, lv = level[node.val]
                best = ll, lv
                return 0, level[node.val]

            depth, best = find(node.left)
            if depth is not None:
                l, v = level[node.val]
                if l + depth + 1 < best[0]:
                    best = l + depth + 1, v
                return depth + 1, best

            depth, best = find(node.right)
            if depth is not None:
                l, v = level[node.val]
                if l + depth + 1 < best[0]:
                    best = l + depth + 1, v
                return depth + 1, best

            return None, None

        level = {}
        getLevel(root)
        depth, best = find(root)
        return best[1]

# root = [1,2,3,4,null,null,null,5,null,6]
k = 2
r = TreeNode(1)
x = r.left = TreeNode(2)
y = r.right = TreeNode(3)
r.left.left = TreeNode(4)
r.left.left.left = TreeNode(5)
r.left.left.left.left = TreeNode(6)
print(Solution().findClosestLeaf(r, k))
