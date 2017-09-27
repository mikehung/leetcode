#!/usr/bin/env python


class Solution(object):
    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        digit = set(d for d in time)
        while True:
            h, m = int(time[0:2]), int(time[3:])
            m += 1
            if m == 60:
                m = 0
                h += 1
                if h == 24:
                    h = 0
            time = '{:0>2}:{:0>2}'.format(h, m)
            if set(time) <= set(digit):
                return time


def test(time):
    print(time, Solution().nextClosestTime(time))


test('19:34')
test('23:59')
test('01:02')
test('00:00')
test('11:11')
test('22:22')
test('13:45')
