class Solution:
    def numRabbits(self, answers):
        """
        :type answers: List[int]
        :rtype: int
        """
        dic = {}
        ret = 0
        for ans in answers:
            if ans not in dic or ans+1 == dic[ans]:
                dic[ans] = 1
                ret += ans + 1
            else:
                dic[ans] += 1

        return ret

answers = [10,10,10]
print(Solution().numRabbits(answers))
answers = [1, 1, 2]
print(Solution().numRabbits(answers))
answers = []
print(Solution().numRabbits(answers))
answers = [0,0,1,1,1]
print(Solution().numRabbits(answers))
answers = [2,2,2,2,2,2]
print(Solution().numRabbits(answers))
