#!/usr/bin/env python
# Definition for binary tree with next pointer.

class TreeLinkNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right
        self.next = None


class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if root is None:
            return

        parents = [root]
        while parents:
            children = []
            for left, right in zip(parents[:-1], parents[1:]):
                left.next = right

            for node in parents:
                if node.left:
                    children.append(node.left)
                if node.right:
                    children.append(node.right)

            parents = children


root = TreeLinkNode(1,
    left=TreeLinkNode(2,
        left=TreeLinkNode(4,
            left=TreeLinkNode(8)
        ),
        right=TreeLinkNode(5)
    ),
    right=TreeLinkNode(3,
        right=TreeLinkNode(7,
            left=TreeLinkNode(14)
        )
    )
)

def show(root):
    parents = [root]

    while parents:
        children = []
        for node in parents:
            print(node.val, node.next.val if node.next else None)
            if node.left:
                children.append(node.left)
            if node.right:
                children.append(node.right)

        parents = children

show(root)
Solution().connect(root)
show(root)
