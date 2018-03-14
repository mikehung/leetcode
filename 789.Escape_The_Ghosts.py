class Solution:
    def escapeGhosts(self, ghosts, target):
        """
        :type ghosts: List[List[int]]
        :type target: List[int]
        :rtype: bool
        """
        dis = abs(target[0])+abs(target[1])
        return all(dis < abs(x-target[0])+abs(y-target[1]) for x, y in ghosts)


ghosts = [[1, 0], [0, 3]]
target = [0, 1]
print(Solution().escapeGhosts(ghosts, target))

ghosts = [[1, 0]]
target = [2, 0]
print(Solution().escapeGhosts(ghosts, target))

ghosts = [[2, 0]]
target = [1, 0]
print(Solution().escapeGhosts(ghosts, target))

ghosts = [[0, 3]]
target = [0, 4]
print(Solution().escapeGhosts(ghosts, target))
