#!/usr/bin/env python

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_water = 0
        i, j = 0, len(height)-1
        while i < j:
            if height[i] < height[j]:
                min_wall = height[i]
                max_water = max(max_water, min_wall*(j-i))
                while i < j and min_wall >= height[i]: i += 1
            else:
                min_wall = height[j]
                max_water = max(max_water, min_wall*(j-i))
                while i < j and min_wall >= height[j]: j -= 1
        return max_water
