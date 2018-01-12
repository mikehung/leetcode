import collections


class Solution:
    def containVirus(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def connect(grid):
            index = 0
            seen = [[False for c in range(n)] for r in range(m)]
            for r in range(m):
                for c in range(n):
                    if not seen[r][c] and grid[r][c] > 0:
                        index += 1
                        dfs(grid, seen, r, c, index)

        def dfs(grid, seen, r, c, index):
            if seen[r][c]:
                return
            seen[r][c] = True
            grid[r][c] = index
            for dr, dc in self.neighbors:
                if 0 <= r+dr < m and 0 <= c+dc < n and grid[r+dr][c+dc] > 0:
                    dfs(grid, seen, r+dr, c+dc, index)

        def infect(grid):
            counter = collections.Counter()
            for r in range(m):
                for c in range(n):
                    if grid[r][c] == 0:
                        regions = set()
                        for dr, dc in self.neighbors:
                            if 0 <= r+dr < m and 0 <= c+dc < n and grid[r+dr][c+dc] > 0:
                                regions.add(grid[r+dr][c+dc])
                        counter += collections.Counter(regions)

            return counter

        def add_walls(index):
            walls = 0
            for r in range(m):
                for c in range(n):
                    if grid[r][c] == index:
                        grid[r][c] = -1
                        for dr, dc in self.neighbors:
                            if 0 <= r+dr < m and 0 <= c+dc < n and grid[r+dr][c+dc] == 0:
                                walls += 1

            return walls

        def spread(grid):
            g = [[_ for _ in row] for row in grid]
            for r in range(m):
                for c in range(n):
                    if g[r][c] == 0:
                        for dr, dc in self.neighbors:
                            if 0 <= r+dr < m and 0 <= c+dc < n and g[r+dr][c+dc] > 0:
                                grid[r][c] = 1
                                break

        if not grid or not grid[0]:
            return 0

        self.neighbors = ((1, 0), (-1, 0), (0, 1), (0, -1))
        m, n, walls = len(grid), len(grid[0]), 0
        while True:
            connect(grid)
            counter = infect(grid)
            if not counter:
                break
            walls += add_walls(counter.most_common(1)[0][0])
            spread(grid)

        return walls
