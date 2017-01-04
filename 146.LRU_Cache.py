#!/usr/bin/env python

class Node(object):
    def __init__(self, key, value):
        self.value = value
        self.key = key
        self.prev = self
        self.next = self

class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.size = 0
        self.list_head = Node('HEAD', -1)
        self.node_map = dict()

    def add_to_list_head(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

        node.prev = self.list_head.prev
        self.list_head.prev.next = node

        node.next = self.list_head
        self.list_head.prev = node

    def del_the_list_next(self):
        removed_node = self.list_head.next
        self.list_head.next = removed_node.next
        removed_node.next.prev = self.list_head
        del self.node_map[removed_node.key]
        del removed_node
        self.size -= 1

    def get(self, key):
        """
        :rtype: int
        """
        if not self.size or key not in self.node_map:
            return -1

        node = self.node_map[key]
        self.add_to_list_head(node)

        return node.value


    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        if not self.capacity:
            return

        if key in self.node_map:
            node = self.node_map[key]
            node.value = value
        else:
            if self.size == self.capacity:
                self.del_the_list_next()

            self.size += 1
            node = Node(key, value)
            self.node_map[key] = node

        self.add_to_list_head(node)
