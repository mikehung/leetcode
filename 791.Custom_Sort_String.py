class Solution:

    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        def compare(x, y):
            return cmp(weight.get(x, 0), weight.get(y, 0))

        weight = {v: k for k, v in enumerate(S)}

        return ''.join(sorted(T, cmp=compare))

S = "cbajd"
T = "abcdjfida81432q9abc131eabc"
print(Solution().customSortString(S, T))
