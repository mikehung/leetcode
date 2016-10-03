#!/usr/bin/env python

import collections

# Definition for a point.
class Point(object):
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        # y = ax + b
        # a = (p1.y - p2.y)/(p1.x - p2.x)
        # b = y - ax

        # 1,2   2,2,  3,2
        # 1,1         3,1
        max_points = 0
        for i in range(len(points)):
            p1 = points[i]
            count = collections.defaultdict(int)
            same_point = 0
            for j in range(i, len(points)):
                p2 = points[j]
                if p1.x == p2.x and p1.y == p2.y:
                    same_point += 1
                    continue

                # solve (a,b) for y = ax + b
                a = b = 0
                if p1.x == p2.x:
                    a = float('inf')
                    b = p1.x
                else:
                    a = (p1.y - p2.y)/float(p1.x - p2.x)
                    b = p1.y - a * p1.x
                count[(a, b)] += 1
            if count:
                max_points = max(max_points, max(count.values())+same_point)
            else:
                max_points = max(max_points, same_point)
        return max_points

points = [Point(1,1), Point(3,1), Point(1,2), Point(2,2), Point(3,2), Point(2,2)]
#points = [Point(1,1), Point(1,1)]
print(Solution().maxPoints(points))
