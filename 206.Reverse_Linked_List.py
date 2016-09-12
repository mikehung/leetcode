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

    def printList(self, list=None):
        node = list or self.list
        n = []
        while node:
            n.append(str(node.val))
            node = node.next
        print(', '.join(n))

    def getList(self):
        return self.list

    def reverseList(self, head):
        return self.reverseList_interative(head)
        return self.reverseList_recursive(head)

    def reverseList_recursive(self, head):
        if head or head.next:
            return head

        node = self.reverseList_recursive(node.next)
        head.next.next = head
        head.next = None

        return node

    def reverseList_interative(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        prev = None
        now = head
        while now:
            next = now.next
            now.next = prev
            prev = now
            now = next

        return prev

s  = Solution()
s.addNode(1)
s.addNode(2)
s.addNode(3)
s.addNode(4)
s.addNode(5)
s.addNode(6)
s.printList()
s.printList(s.reverseList(s.getList()))
