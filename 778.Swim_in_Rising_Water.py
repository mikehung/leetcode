class Solution:
    def swimInWater(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def dfs_visit(x, y, visit, depth):
            if not (0 <= x < n) or not (0 <= y < n):
                return False
            if (x, y) in visit:
                return False
            if grid[x][y] > depth:
                return False
            if x == n-1 and y == n-1:
                return True
            visit.add((x, y))
            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                if dfs_visit(x+dx, y+dy, visit, depth):
                    return True
            return False

        def has_route(depth):
            return dfs_visit(0, 0, set(), depth)

        n = len(grid)
        lo, hi = 0, n*n-1
        while lo < hi:
            mid = lo + (hi-lo)//2
            if not has_route(mid):
                lo = mid+1
            else:
                hi = mid
        return lo


def test(grid, ans):
    r = Solution().swimInWater(grid)
    print(r == ans, r, ans)


grid = [[0,2],[1,3]]
test(grid, 3)
grid = [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
test(grid, 16)
