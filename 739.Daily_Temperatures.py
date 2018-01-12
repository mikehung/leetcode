class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        result = [0] * len(temperatures)
        lst = []
        for i in range(len(temperatures)-1, -1, -1):
            while lst and lst[-1][0] <= temperatures[i]:
                lst.pop()
            if lst:
                result[i] = lst[-1][1] - i
            lst.append((temperatures[i], i))

        return result


temperatures = [73, 74, 75, 71, 69, 72, 76, 76]
result = [1, 1, 4, 2, 1, 1, 0, 0]
print(Solution().dailyTemperatures(temperatures))
