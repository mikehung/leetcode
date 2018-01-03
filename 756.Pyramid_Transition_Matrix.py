import itertools
import collections


class Solution:
    def pyramidTransition(self, bottom, allowed):
        """
        :type bottom: str
        :type allowed: List[str]
        :rtype: bool
        """
        def slove(bottom):
            if len(bottom) == 2:
                return (bottom[0], bottom[1]) in allow_dict

            lst = []
            for key in zip(bottom, bottom[1:]):
                if key not in allow_dict:
                    return False
                lst.append(allow_dict[key])

            for product in itertools.product(*lst):
                if slove(''.join(product)):
                    return True

            return False


        allow_dict = collections.defaultdict(set)
        for c1, c2, c3 in allowed:
            allow_dict[(c1, c2)].add(c3)

        return slove(bottom)


bottom = 'XYZ'
allowed = ["XYD", "YZE", "DEA", "FFF"]
print(Solution().pyramidTransition(bottom, allowed))

bottom = "XXYX"
allowed = ["XXX", "XXY", "XYX", "XYY", "YXZ"]
print(Solution().pyramidTransition(bottom, allowed))

bottom = "ABCD"
allowed = ["BCE", "BCF", "ABA", "CDA", "AEG", "FAG", "GGG"]
print(Solution().pyramidTransition(bottom, allowed))
