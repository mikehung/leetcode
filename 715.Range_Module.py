#!/usr/bin/env python3

import bisect


class RangeModule(object):
    def __init__(self):
        self.ranges = [0]
        self.tracks = [False]

    def makeRange(self, left, right, tracked):
        def updateRange(value, is_left):
            if is_left:
                index = bisect.bisect_left(self.ranges, value)
            else:
                index = bisect.bisect(self.ranges, value)
            self.ranges.insert(index, value)
            self.tracks.insert(index, self.tracks[index-1])

            return index

        i, j = updateRange(left, True), updateRange(right, False)
        self.ranges[i:j] = [left]
        self.tracks[i:j] = [tracked]

    def addRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: void
        """
        self.makeRange(left, right, True)

    def queryRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: bool
        """
        i, j = bisect.bisect(self.ranges, left)-1, bisect.bisect_left(self.ranges, right)
        return all(self.tracks[i:j])


    def removeRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: void
        """
        self.makeRange(left, right, False)
