#!/usr/bin/env python3

class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        points = []
        result = 0
        for op in ops:
            if op == 'C':
                result -= points.pop()
                continue
            if op == '+':
                num = points[-1] + points[-2]
            elif op == 'D':
                num = points[-1] * 2
            else:
                num = int(op)

            points.append(num)
            result += num

        return result

def run(ops):
    print(Solution().calPoints(ops))

run(["5","2","C","D","+"])
run(["5","-2","4","C","D","9","+","+"])
