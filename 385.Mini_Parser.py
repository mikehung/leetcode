#!/usr/bin/env python

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution(object):
    def deserialize(self, s):
        """
        :type s: str
        :rtype: NestedInteger
        """
        stack = []
        value, minus = None, False
        for c in s:
            if c.isdigit():
                value = value*10+int(c) if value else int(c)
            elif c == '-':
                value, minus = None, True
            else:
                if c == ',':
                    if value != None:
                        stack[-1].add(NestedInteger(-value if minus else value))
                elif c == ']':
                    if value != None:
                        stack[-1].add(NestedInteger(-value if minus else value))
                    top = stack.pop()
                    if stack:
                        stack[-1].add(top)
                elif c == '[':
                    stack.append(NestedInteger())
                value, minus = None, False
        return NestedInteger(-value if minus else value) if value != None else top.getList()

        # s=123 -> NestedInteger(123)
        # s=[123] -> NestedInteger() + NestedInteger(123)
        # s=[123,123]
        # s=[123,[]]
        # s=[123,[456,[789]]]
        # s=[1,1]
        # s=[1,[],1]
