class Solution:
    def canTransform(self, start, end):
        """
        :type start: str
        :type end: str
        :rtype: bool
        """
        def get_nxt_lr(idx, string):
            if idx >= len(string):
                return idx, None
            for i in range(idx, len(string)):
                if string[i] in 'RL':
                    return i, string[i]
            return i, None


        if len(start) != len(end):
            return False

        si = ei = 0
        while si < len(start) or ei < len(start):
            si, sc = get_nxt_lr(si, start)
            ei, ec = get_nxt_lr(ei, end)
            if sc != ec:
                return False
            elif sc == 'L':
                if si < ei:
                    return False
            elif sc == 'R':
                if si > ei:
                    return False
            si, ei = si+1, ei+1

        return True


def test(s, e):
    print(s, e)
    r = Solution().canTransform(s, e)
    print(r)

test('XXL', 'LXX')
test('XXR', 'RXX')
s = 'RXXLRXRXL'
e = 'XRLXXRRLX'
test(s, e)
s = 'XXRLLXRRXXL'
e = 'RXXXLLXXRRL'
test(s, e)
s="XXRXXLXXXX"
e="XXXXRXXLXX"
test(s, e)
