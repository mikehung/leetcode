#!/usr/bin/env python

# Definition for binary tree with next pointer.
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        def helper(node, parent, is_right, is_right_most):
            if is_right_most:
                node.next = None
            elif is_right:
                node.next = parent.next.left
            else:
                node.next = parent.right

            if node.left is None:
                return
            helper(node.left, node, is_right=False, is_right_most=False)
            helper(node.right, node, is_right=True, is_right_most=is_right_most)

        if root is None or root.left is None:
            return
        helper(root.left, root, is_right=False, is_right_most=False)
        helper(root.right, root, is_right=True, is_right_most=True)

length = 2**5-1
nodes = [TreeLinkNode(_) for _ in range(length)]
nodes[0].left = nodes[1]
nodes[0].right = nodes[2]
nodes[1].left

for i in range(length/2):
    nodes[i].left = nodes[i*2+1]
    nodes[i].right = nodes[i*2+2]

Solution().connect(nodes[0])
for i in range(length):
    n = [nodes[i].val]
    if nodes[i].next:
        n += [nodes[i].next.val]
    else:
        n += ['None']
    if nodes[i].left:
        n += [nodes[i].left.val, nodes[i].right.val]
    print(', '.join([str(_) for _ in n]))
