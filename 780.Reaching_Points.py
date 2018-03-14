class Solution:
    def reachingPoints(self, sx, sy, tx, ty):
        """
        :type sx: int
        :type sy: int
        :type tx: int
        :type ty: int
        :rtype: bool
        """
        while tx and ty:
            if (tx, ty) == (sx, sy):
                return True
            elif tx == sx:
                if tx > ty or ty < sy:
                    return False
                else:
                    return (ty-sy)%tx == 0
            elif ty == sy:
                if ty > tx or tx < sx:
                    return False
                else:
                    return (tx-sx)%ty == 0
            else:
                if tx == ty:
                    return False
                elif tx > ty:
                    tx = tx%ty
                else:
                    ty = ty%tx
        return (tx, ty) == (sx, sy)


sx = sy = 1; tx = 3; ty = 5
print(Solution().reachingPoints(sx, sy, tx, ty))
sx = sy = 1; tx = ty = 2
print(Solution().reachingPoints(sx, sy, tx, ty))
sx = sy = tx = ty = 1
print(Solution().reachingPoints(sx, sy, tx, ty))
sx=35
sy=13
tx=455955547
ty=420098884
print(Solution().reachingPoints(sx, sy, tx, ty))
