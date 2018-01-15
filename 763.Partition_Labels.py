class Solution:
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        def merge(partition, length, label):
            for c in partition:
                if partition[c] > label:
                    partition[c] = label
            length[label:] = [sum(length[label:])]

        length = []
        partition = {}
        label = 0
        for c in S:
            if c not in partition:
                partition[c] = label
                length.append(1)
                label += 1
            else:
                merge(partition, length, partition[c])
                length[-1] += 1
                label = partition[c] + 1

        return length



S = "ababcbacadefegdehijhklij"
print(Solution().partitionLabels(S))
S = 'abcb'
print(Solution().partitionLabels(S))
S = 'abcbdefga'
print(Solution().partitionLabels(S))
