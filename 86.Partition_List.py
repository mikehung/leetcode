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

    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        node = head
        large_small_head = [None, None]
        large_small_list = [None, None]

        while node:
            if not large_small_list[node.val<x]:
                large_small_head[node.val<x] = node
                large_small_list[node.val<x] = node
            else:
                large_small_list[node.val<x].next = node
                large_small_list[node.val<x] = node
            node = node.next

        head = large_small_head[1] or large_small_head[0]
        if large_small_list[1]:
            large_small_list[1].next = large_small_head[0]
        if large_small_list[0]:
            large_small_list[0].next = None

        return head

sol = Solution()
for i in [1,4,3,2,5,2]:
    sol.addNode(i)
h = sol.partition(sol.list, 3)
sol.printList(h)

sol = Solution()
for i in []:
    sol.addNode(i)
h = sol.partition(sol.list, 3)
sol.printList(h)

sol = Solution()
for i in [-1,-2,1,0,1]:
    sol.addNode(i)
h = sol.partition(sol.list, 3)
sol.printList(h)

sol = Solution()
for i in [-1,-2,1,0,1]:
    sol.addNode(i)
h = sol.partition(sol.list, -3)
sol.printList(h)
