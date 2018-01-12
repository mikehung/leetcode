import bisect


class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution:
    def employeeFreeTime(self, schedule):
        """
        :type schedule: List[List[Interval]]
        :rtype: List[Interval]
        """
        time = []
        free = []

        for sched in schedule:
            for interval in sched:
                start, end = interval.start, interval.end
                si = bisect.bisect_left(time, start)
                bi = bisect.bisect(time, end)
                if si > 0 and free[si-1]:
                    start = time[si-1]
                    si -= 1
                if bi < len(free) and not free[bi]:
                    end = time[bi]
                time[si:bi] = [start, end]
                free[si:bi] = [True, False]

        ans = []
        for i in range(len(time)-1):
            if not free[i] and free[i+1]:
                ans.append([time[i], time[i+1]])

        return ans

    # using merge interval
    #  sort the interval, and combine all intervals in a linear traversal
    #  key idea:
    #   if interval[i] doesn't overlap with interval[i-1],
    #   then interval[i+1] cannot overlap with interval[i-1]
    def employeeFreeTime2(self, schedule):
        schedules = []
        for sched in schedule:
            for interval in sched:
                schedules.append((interval.start, interval.end))

        merged_interval = []
        for interval in sorted(schedules):
            try:
                top_interval = merged_interval[-1]
            except IndexError:
                merged_interval.append(interval)
                continue

            if top_interval[1] < interval[0]:
                # Non-overlapping => just append interval
                merged_interval.append(interval)
            elif top_interval[1] < interval[1]:
                # Overlapping, and current interval's end is larger => replace last interval
                merged_interval[-1] = top_interval[0], interval[1]

        free_interval = []
        for i1, i2 in zip(merged_interval, merged_interval[1:]):
            free_interval.append([i1[1], i2[0]])

        return free_interval



def I(lst):
    return Interval(lst[0], lst[1])


def test(schedule, exp):
    schedule = [[I(lst) for lst in sched] for sched in schedule]
    ans = Solution().employeeFreeTime(schedule)
    ans2 = Solution().employeeFreeTime2(schedule)
    print(ans == exp, exp, ans)
    print(ans2 == exp, exp, ans2)


schedule = [[[1,2],[5,6]],[[1,3]],[[4,10]]]
exp = [[3,4]]
test(schedule, exp)

schedule = [[[1,3],[6,7]],[[2,4]],[[2,5],[9,12]]]
exp = [[5,6],[7,9]]
test(schedule, exp)

schedule = [[[7,24],[29,33],[45,57],[66,69],[94,99]],[[6,24],[43,49],[56,59],[61,75],[80,81]],[[5,16],[18,26],[33,36],[39,57],[65,74]],[[9,16],[27,35],[40,55],[68,71],[78,81]],[[0,25],[29,31],[40,47],[57,87],[91,94]]]
exp = [[26,27],[36,39],[87,91]]
test(schedule, exp)

schedule = [[[6,24], [5, 16], [18, 26]]]
exp = []
test(schedule, exp)
