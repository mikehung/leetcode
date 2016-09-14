#!/usr/bin/env python

import random

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):

    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.head = head
        self.length = 0

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        if self.length == 0:
            ptr = self.head
            while ptr:
                self.length += 1
                ptr = ptr.next

        ptr = self.head
        for i in range(random.randrange(self.length)):
            ptr = ptr.next

        print(ptr.val)
        return ptr.val


# Your Solution object will be instantiated and called as such:
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(0)

l = [0] * 3
obj = Solution(head)
for i in range(100):
    l[obj.getRandom()] += 1
print(l)

