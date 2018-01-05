# Time: O(n**3)
# Space: O(n**3)
class Solution:
    def cherryPicking(self, grid):
        def slove(key):
            if key in picking:
                return picking[key]

            r1, c1, r2, c2 = key
            if N in key or grid[r1][c1] == -1 or grid[r2][c2] == -1:
                return float('-inf')
            if r1 == c1 == r2 == c2 == N-1:
                return grid[r1][c1]

            picking[key] = max(slove((r1+1, c1, r2+1, c2)),
                               slove((r1, c1+1, r2+1, c2)),
                               slove((r1+1, c1, r2, c2+1)),
                               slove((r1, c1+1, r2, c2+1))) + \
                           grid[r1][c1] + ((r1, c1) != (r2, c2)) * grid[r2][c2]

            return picking[key]

        N = len(grid)
        picking = dict()
        return max(0, slove((0, 0, 0, 0)))

grid = [
    [0, 1, -1],
    [1, 0, -1],
    [1, 1,  1]
]

print(Solution().cherryPicking(grid))

grid = [[1,1,-1],[1,-1,1],[-1,1,1]]
print(Solution().cherryPicking(grid))
grid = [[1,-1,1,1,1,1,1,1,1,-1],[-1,1,1,-1,-1,1,-1,1,1,1],[-1,1,1,1,1,1,1,1,1,1],[1,1,-1,1,1,1,1,1,1,-1],[-1,1,1,1,1,1,1,1,-1,1],[1,-1,-1,1,1,1,-1,1,-1,1],[1,1,-1,1,1,-1,-1,1,1,1],[1,1,1,-1,-1,-1,1,1,1,-1],[1,1,-1,-1,-1,1,1,1,1,-1],[1,1,-1,-1,1,1,1,1,1,1]]
print(Solution().cherryPicking(grid))
grid = [
    [1, 1, 1, 0, 0],
    [0, 0, 1, 0, 1],
    [1, 0, 1, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 1, 1, 1]
]
print(Solution().cherryPicking(grid))
