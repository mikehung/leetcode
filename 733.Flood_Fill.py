# Time: O(N), N = len(image) * len(image[0])
# Space: O(N)

class Solution:
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        # depth-first approach
        def flood(sr, sc):
            image[sr][sc] = newColor
            if sr-1 >= 0 and image[sr-1][sc] == oldColor:
                flood(sr-1, sc)
            if sc-1 >= 0 and image[sr][sc-1] == oldColor:
                flood(sr, sc-1)
            if sr+1 < len(image) and image[sr+1][sc] == oldColor:
                flood(sr+1, sc)
            if sc+1 < len(image[0]) and image[sr][sc+1] == oldColor:
                flood(sr, sc+1)

        if image[sr][sc] == newColor:
            return image

        oldColor = image[sr][sc]
        flood(sr, sc)

        return image

image = ([1, 1, 1], [1, 1, 0], [1, 0, 1])
image = Solution().floodFill(image, 1, 1, 2)
print(image)
