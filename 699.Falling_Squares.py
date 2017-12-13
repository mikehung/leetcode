#!/usr/bin/env python

class Solution(object):
    def fallingSquares(self, positions):
        """
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        falling_positions = []
        max_height = 0
        max_heights = []
        for left, length in positions:
            max_falling_height = 0
            for falling_left, falling_length, falling_height in falling_positions:
                # no overlapping
                if left >= falling_left + falling_length or left + length <= falling_left:
                    continue
                max_falling_height = max(max_falling_height, falling_height)
            curr_falling_height = max_falling_height + length
            falling_positions.append((left, length, curr_falling_height))
            max_height = max(max_height, curr_falling_height)
            max_heights.append(max_height)

        return max_heights


def test(positions, e):
    r = Solution().fallingSquares(positions)
    print(e == r, positions, e, r)

test([[1, 2], [2, 3], [6, 1]], [2, 5, 5])
test([[100, 100], [200, 100]], [100, 100])
