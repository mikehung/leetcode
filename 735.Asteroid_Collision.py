# Time: O(n)
# Space: O(n)

class Solution:
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        ret = []
        for ast in asteroids:
            if not ret:
                ret.append(ast)
            elif ret[-1] > 0 and ast < 0:
                # has collision
                explode = False
                while ret and ret[-1] > 0:
                    if ret[-1] > abs(ast):
                        explode = True
                        break
                    elif ret[-1] == abs(ast):
                        explode = True
                        ret.pop()
                        break
                    else:
                        ret.pop()
                if not explode:
                    ret.append(ast)
            else:
                ret.append(ast)

        return ret

print(Solution().asteroidCollision([5, 10, -5]), [5, 10])
print(Solution().asteroidCollision([9, -9]), [])
print(Solution().asteroidCollision([10, 2, -5]), [10])
print(Solution().asteroidCollision([-2, -1, 1, 2]), [-2, -1, 1, 2])
print(Solution().asteroidCollision([-2, -2, 1, -2]), [-2, -2, -2])
