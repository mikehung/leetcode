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

    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if m == n:
            return head

        prev = None
        now = head

        for i in range(1, n + 1):
            if not now:
                break

            if i < m:
                prev = now
                now = now.next
                continue

            if i == m:
                c1 = prev
                c2 = now
            next = now.next
            now.next = prev
            prev = now
            now = next

        if c1:
            c1.next = prev
        else:
            head = prev
        if c2:
            c2.next = now

        return head


s  = Solution()
s.addNode(1)
s.addNode(2)
s.printList()
s.printList(s.reverseBetween(s.getList(), 1, 2))
