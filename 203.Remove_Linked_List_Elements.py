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

        return self.list

    def printList(self, list):
        node = list
        n = []
        while node:
            n.append(str(node.val))
            node = node.next
        print('[' + ', '.join(n) + ']')

    def getList(self):
        return self.list

    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        print('start: ' + str(val))
        self.printList(head)
        dummy = ListNode(val - 1)
        dummy.next = head

        prev = dummy
        curr = head

        while curr:
            if curr.val == val:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next

        return dummy.next

sol = Solution()
sol.printList(sol.removeElements(sol.list, 1))

sol = Solution()
s = sol.addNode(1)
sol.printList(sol.removeElements(s, 1))

sol = Solution()
s = sol.addNode(1)
s = sol.addNode(1)
s = sol.addNode(1)
sol.printList(sol.removeElements(s, 1))

sol = Solution()
s = sol.addNode(2)
s = sol.addNode(2)
sol.printList(sol.removeElements(s, 1))

sol = Solution()
s = sol.addNode(1)
s = sol.addNode(2)
s = sol.addNode(1)
s = sol.addNode(2)
s = sol.addNode(1)
sol.printList(sol.removeElements(s, 1))
