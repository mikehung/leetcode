#!/usr/bin/env python
# Time: O(nlogn), n: number of booking
# Space: O(n)

import bisect


class MyCalendar(object):

    def __init__(self):
        self.time = [0]
        self.can_book = [True]

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        if start >= end:
            return False

        si = bisect.bisect(self.time, start)
        ei = bisect.bisect_left(self.time, end)
        if not all(self.can_book[si-1:ei]):
            return False

        has_end = ei < len(self.time) and self.time[ei] == end

        if self.time[si-1] == start:
            eii = ei
            self.can_book[si-1] = False
        else:
            eii = ei+1
            self.time.insert(si, start)
            self.can_book.insert(si, False)

        if not has_end:
            self.time.insert(eii, end)
            self.can_book.insert(eii, True)

        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)

obj = MyCalendar()
def test(start, end, e):
    print('Booking {} to {}'.format(start, end))
    res = obj.book(start, end)
    print(res == e, e, res)


test(10, 20, True)
test(15, 25, False)
test(20, 30, True)
test(40, 50, True)
test(38, 50, False)
test(30, 33, True)
test(33, 38, True)
test(37, 39, False)
test(38, 39, True)
test(39, 40, True)
