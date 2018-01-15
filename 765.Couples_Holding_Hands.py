class Solution:
    def minSwapsCouples(self, row):
        """
        :type row: List[int]
        :rtype: int
        """
        def find(trans, x):
            if x not in trans:
                return x
            y = find(trans, trans[x])
            if trans[x] != y:
                trans[x] = y
            return y

        num_swap = 0
        trans = {}
        for i in range(0, len(row), 2):
            x = find(trans, row[i]//2)
            y = find(trans, row[i+1]//2)
            if x != y:
                num_swap += 1
                trans[x] = y
        return num_swap


row = [0, 2, 1, 3]
print(Solution().minSwapsCouples(row))
row = [3, 2, 0, 1]
print(Solution().minSwapsCouples(row))
row = [0, 6, 2, 4, 4, 6, 2, 0]
print(Solution().minSwapsCouples(row))
row = [0,2,4,6,7,1,3,5]
print(Solution().minSwapsCouples(row))
