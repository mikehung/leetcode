#!/usr/bin/env python

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def __init__(self):
        self.list = None
        self.back = None

    def addNode(self, val):
        node = ListNode(val)

        if not self.back:
            self.list = node
            self.back = node
        else:
            self.back.next = node
            self.back = node

    def printList(self, list):
        node = list
        n = []
        while node:
            n.append(str(node.val))
            node = node.next
        print(', '.join(n))

    def getList(self):
        return self.list

    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        next_node = node.next
        node.val = next_node.val
        node.next = next_node.next
        del(next_node)

sol = Solution()
sol.addNode(1)
s = sol.list
sol.addNode(2)
sol.addNode(3)
sol.deleteNode(s.next)
sol.printList(sol.list)
