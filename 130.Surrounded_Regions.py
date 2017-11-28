# Time: O(mn), m = len(board), n = len(board[0])
# Space: O(mn)

class Solution:
    def solve(self, board):
        def bfs(pie, gid, indices):
            while indices:
                next_indices = set()
                for r, c in indices:
                    if 0 <= r < len(board) and 0 <= c < len(board[0]) and \
                       group[r][c] is None and board[r][c] == pie:
                        group[r][c] = gid
                        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                            next_indices.add((r+dr, c+dc))
                indices = next_indices

        if not board or not board[0]:
            return
        range_r, range_c = range(len(board)), range(len(board[0]))
        group = [[None for c in range_c] for r in range_r]
        gid = 0
        for r in range_r:
            for c in range_c:
                if group[r][c] is None:
                    bfs(board[r][c], gid, set([(r, c)]))
                    gid += 1

        no_surr = set()
        no_surr.update([group[0][c] for c in range_c if board[0][c] == "O"])
        no_surr.update([group[-1][c] for c in range_c if board[-1][c] == "O"])
        no_surr.update([group[r][0] for r in range_r if board[r][0] == "O"])
        no_surr.update([group[r][-1] for r in range_r if board[r][-1] == "O"])

        for r in range_r:
            for c in range_c:
                if group[r][c] not in no_surr:
                    board[r][c] = "X"

sol = Solution()
board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
print(len(board), len(board[0]))
sol.solve(board)
