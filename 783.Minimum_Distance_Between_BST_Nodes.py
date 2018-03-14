class Solution:
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            self.min_dis = min(abs(root.val-self.pre_val), self.min_dis)
            self.pre_val = root.val
            inorder(root.right)

        self.min_dis = float('inf')
        self.pre_val = float('inf')
        inorder(root)
        return self.min_dis
