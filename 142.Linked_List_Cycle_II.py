#!/usr/bin/env python

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head

        slow = head
        fast = head

        while slow and fast:
            if not fast.next:
                return None

            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                break

        begin = head
        while begin and slow:
            if begin == slow:
                return begin
            begin = begin.next
            slow = slow.next

        return None

l = ListNode(1)
l.next = ListNode(2)
l.next.next = ListNode(3)
l.next.next.next = l
c = Solution().detectCycle(l)
if c:
	print(c.val)
else:
	print('no cycle')
