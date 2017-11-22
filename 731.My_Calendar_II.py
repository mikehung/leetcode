#!/usr/bin/env python
# Time: O(n**2)
# Space: O(n)


class Node(object):
    def __init__(self, start, end):
        self.left = None
        self.right = None
        self.start = start
        self.end = end

class MyCalendarTwo(object):

    def __init__(self):
        self.booked = []
        self.overlap = []

    def book(self, start, end):
        overlap = []
        for s, e in self.overlap:
            if end > s and e > start:
                return False

        for s, e in self.booked:
            if end > s and e > start:
                self.overlap.append((max(start, s), min(end, e)))

        self.booked.append((start, end))
        return True


def test(start, end, e):
    print('Booking {} to {}'.format(start, end))
    res = obj.book(start, end)
    print(res == e, e, res)


TEST = 2
if TEST == 1:
    obj = MyCalendar()
    test(10, 20, True)
    test(19, 20, False)
    test(10, 20, False)
    test(10, 11, False)
    test(30, 40, True)
    test(20, 21, True)
    test(29, 30, True)
    test(23, 27, True)
    test(21, 25, False)
    test(25, 29, False)
    test(21, 23, True)
elif TEST == 2:
    obj = MyCalendarTwo()
    test(10, 20, True)
    test(50, 60, True)
    test(10, 40, True)
    test(5, 15, False)
    test(5, 10, True)
    test(25, 55, True)
    test(20, 25, True)
    test(20, 25, False)
    test(20, 25, False)
