class Solution:
    def pourWater(self, heights, V, K):
        """
        :type heights: List[int]
        :type V: int
        :type K: int
        :rtype: List[int]
        """
        for v in range(V):
            # try to move left
            low_i = None
            i = K - 1
            while i >= 0:
                if heights[i] > heights[i+1]:
                    break
                elif heights[i] < heights[i+1]:
                    low_i = i
                i -= 1

            if low_i is not None:
                heights[low_i] += 1
                continue

            # try to move left
            i = K + 1
            while i < len(heights):
                if heights[i] > heights[i-1]:
                    break
                elif heights[i] < heights[i-1]:
                    low_i = i
                i += 1

            if low_i is not None:
                heights[low_i] += 1
                continue

            heights[K] += 1

        return heights

print(Solution().pourWater([2,1,1,2,1,2,2], 4, 3))
print(Solution().pourWater([1,2,3,4], 2, 2))
print(Solution().pourWater([3,1,3], 5, 1))
