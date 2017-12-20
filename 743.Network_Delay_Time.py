# N_2 wrong!! old: N
import collections
class Solution:
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        edges = collections.defaultdict(list)
        for u, v, w in times:
            edges[u].append((v, w))

        delay = [None] * N
        N_2 = N ** 2

        deque = collections.deque()
        deque.append(K)
        delay[K-1] = 0

        count = 0
        while deque:
            u = deque.popleft()
            for v, w in edges[u]:
                deque.append(v)
                if delay[v-1] is None or delay[v-1] > delay[u-1] + w:
                    delay[v-1] = delay[u-1] + w
            count += 1
            if count > N_2:
                break
        return -1 if None in delay else max(delay)

times = [[2,1,1],[2,3,1],[3,4,1]]
N = 4
K = 2
print(Solution().networkDelayTime(times, N, K))
times = [[4,2,76],[1,3,79],[3,1,81],[4,3,30],[2,1,47],[1,5,61],[1,4,99],[3,4,68],[3,5,46],[4,1,6],[5,4,7],[5,3,44],[4,5,19],[2,3,13],[3,2,18],[1,2,0],[5,1,25],[2,5,58],[2,4,77],[5,2,74]]
N = 5
K = 3
print(Solution().networkDelayTime(times, N, K))
