# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, nxt=None):
        self.val = x
        self.next = nxt

import heapq

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        ans = point = ListNode(0)
        heap = [(root.val, root) for root in lists if root]
        heapq.heapify(heap)
        while heap:
            val, node = heapq.heappop(heap)
            point.next = ListNode(val)
            point = point.next
            node = node.next
            if node:
                heapq.heappush(heap, (node.val, node))

        return ans.next


def printList(root):
    l = []
    while root:
        l.append(root.val)
        root = root.next
    print(l)


def getListNode(lst):
    node = root = ListNode(0)
    for item in lst:
        node.next = ListNode(item)
        node = node.next

    return root.next

l1 = getListNode([1, 6, 7])
l2 = getListNode([2, 3, 10])
l3 = getListNode([2, 5, 9])
printList(Solution().mergeKLists([l1, l2, l3]))

l1 = getListNode([1, 2, 2])
l2 = getListNode([1, 1, 2])
printList(Solution().mergeKLists([l1, l2]))
