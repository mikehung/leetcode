# Time: O(p + w), p = len(pairs), w = len(words1)
# Space: O(p)

class Solution:
    def areSentencesSimilar(self, words1, words2, pairs):
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        """
        if len(words1) != len(words2):
            return False
        pairs = set((w1, w2) for w1, w2 in pairs)
        for w1, w2 in zip(words1, words2):
            if w1 == w2:
                continue
            if (w1, w2) not in pairs and (w2, w1) not in pairs:
                return False

        return True

