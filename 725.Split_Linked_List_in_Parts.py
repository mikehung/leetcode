#!/usr/bin/env python
# Time: O(n+k)
# Space: O(k)

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def splitListToParts(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        num = 0
        node = root
        while node:
            num += 1
            node = node.next

        ret = []
        cnt, rem = divmod(num, k)
        node, prev = root, None
        for i in range(k):
            if prev:
                prev.next = None
            ret.append(node)
            for c in range(cnt):
                node, prev = node.next, node
            if i < rem:
                node, prev = node.next, node

        return ret
