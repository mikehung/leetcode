#!/usr/bin/env python

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        def buildList(root, lst):
            if not root:
                lst.append('N')
            else:
                lst.append(str(root.val))
                buildList(root.left, lst)
                buildList(root.right, lst)
        lst = []
        buildList(root, lst)
        return ','.join(lst)


    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        def buildTree(it):
            val = next(it)
            if val == 'N':
                root = None
            else:
                root = TreeNode(int(val))
                root.left = buildTree(it)
                root.right = buildTree(it)
            return root

        return buildTree(iter(data.split(',')))


# Your Codec object will be instantiated and called as such:
codec = Codec()
#codec.deserialize(codec.serialize(root))
root = None
print(root == codec.deserialize(codec.serialize(root)))

root = TreeNode(20)
root.left = TreeNode(10)
root.right = TreeNode(5)
root.left.left = TreeNode(1)
root.left.left.right = TreeNode(4)
root.right.left = TreeNode(9)
root.right.left.left = TreeNode(91)
print(codec.serialize(root))
d =  codec.deserialize(codec.serialize(root))
print(codec.serialize(d))

root = TreeNode(20)
root.right = TreeNode(5)
print(codec.serialize(root))
d =  codec.deserialize(codec.serialize(root))
print(codec.serialize(d))
