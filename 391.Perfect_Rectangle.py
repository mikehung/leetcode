#!/usr/bin/env python

class Solution(object):
    def isRectangleCover(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: bool
        """
        def update_corner(corner, point, mask):
            if point in corner:
                if corner[point] & mask: return False
            else:
                corner[point] = 0
            corner[point] |= mask
            return True

        corner = dict()
        min_x, min_y, max_x, max_y = float('inf'), float('inf'), float('-inf'), float('-inf')
        for x, y, X, Y in rectangles:
            if not update_corner(corner, (x, y), 1): return False
            if not update_corner(corner, (X, y), 2): return False
            if not update_corner(corner, (x, Y), 4): return False
            if not update_corner(corner, (X, Y), 8): return False
            min_x, min_y, max_x, max_y = min(min_x, x), min(min_y, y), max(max_x, X), max(max_y, Y)

        for (x, y), mask in corner.items():
            if (x, y) not in ((min_x, min_y), (max_x, min_y), (min_x, max_y), (max_x, max_y)) \
                and mask not in (3, 5, 10, 12, 15):
                return False
        return True

rectangles = [
  [1,1,3,3],
  [3,1,4,2],
  [3,2,4,4],
  [1,3,2,4],
  [2,3,3,4]
]
print(Solution().isRectangleCover(rectangles))

rectangles = [
  [1,1,2,3],
  [1,3,2,4],
  [3,1,4,2],
  [3,2,4,4]
]
print(Solution().isRectangleCover(rectangles))

rectangles = [
  [1,1,3,3],
  [3,1,4,2],
  [1,3,2,4],
  [3,2,4,4]
]
print(Solution().isRectangleCover(rectangles))

rectangles = [
  [1,1,3,3],
  [3,1,4,2],
  [1,3,2,4],
  [2,2,4,4]
]
print(Solution().isRectangleCover(rectangles))

rectangles = [[0,0,1,1],[0,2,1,3],[1,1,2,2],[2,0,3,1],[2,2,3,3],[1,0,2,3],[0,1,3,2]]
print(Solution().isRectangleCover(rectangles))
