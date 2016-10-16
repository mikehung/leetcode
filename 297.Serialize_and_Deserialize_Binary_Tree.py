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
        if not root: return ''

        result = []
        dad = [root]

        while dad:
            son = []
            for node in dad:
                if node:
                    result += [str(node.val)]
                    son += [node.left, node.right]
                else:
                    result += ['n']
            dad = son

        i = len(result)-1
        while i:
            if result[i] != 'n': break
            i -= 1

        return ','.join(result[:i+1])


    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data: return None

        items = data.split(',')
        root = TreeNode(items[0])
        nodes = [(root, True), (root, False)]

        for item in items[1:]:
            if item == 'n':
                nodes = nodes[1:]
            else:
                node, isLeft = nodes[0]
                son = TreeNode(item)
                if isLeft:
                    node.left = son
                else:
                    node.right = son
                nodes = nodes[1:] + [(son, True), (son, False)]

        return root


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
