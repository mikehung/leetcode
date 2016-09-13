#!/usr/bin/env python
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return head
        list = []
        node = head
        while node:
            list.append(node)
            node = node.next

        n = k % len(list)
        head = list[-n]
        list[-1].next = list[0]
        list[-n-1].next = None

        return head


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

    def printList(self, list=None):
        node = list or self.list
        n = []
        while node:
            n.append(str(node.val))
            node = node.next
        print(', '.join(n))

    def getList(self):
        return self.list


s  = Solution()
s.addNode(1)
s.addNode(2)
s.addNode(3)
s.addNode(4)
s.addNode(5)
s.addNode(6)
s.printList()
s.printList(s.rotateRight(s.getList(), 10))
