import collections


class Solution:
    # Time: O(n**2), n = len(A)
    # Space: O(n)
    def anagramMappings(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        mapping = []
        indices = set([i for i in range(len(A))])

        for a in A:
            for i in indices:
                if a == B[i]:
                    mapping.append(i)
                    indices.remove(i)
                    break

        return mapping

    # Time: O(n), n = len(A)
    # Space: O(n)
    def anagramMappings2(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        d = collections.defaultdict(list)
        for i, n in enumerate(B):
            d[n].append(i)

        mapping = []
        for n in A:
            mapping.append(d[n].pop())

        return mapping


A = [12, 28, 46, 32, 50]
B = [50, 12, 32, 46, 28]
print(Solution().anagramMappings(A, B))
print(Solution().anagramMappings2(A, B))
A, B = [], []
print(Solution().anagramMappings(A, B))
print(Solution().anagramMappings2(A, B))
A = [1, 2, 1, 3, 1]
B = [2, 1, 1, 1, 3]
print(Solution().anagramMappings(A, B))
print(Solution().anagramMappings2(A, B))
