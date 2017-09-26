#!/usr/bin/env python

# '.' Matches any single character.
# '*' Matches zero or more of the preceding element.
#
# The matching should cover the entire input string (not partial).
#
# The function prototype should be:
# bool isMatch(const char *s, const char *p)

class Solution(object):
    def match(self, s, si, p, pi):
        def charMatch(s, si, p, pi):
            try:
                return p[pi] in (s[si], '.')
            except:
                return False

        def starMatch(t, s, si, p, pi):
            return self.match(s, si, p, pi) or (charMatch(s, si, t, 0) and starMatch(t, s, si+1, p, pi))

        if si == len(s) and pi == len(p):
            return True

        if pi+1 < len(p) and p[pi+1] == '*':
            return starMatch(p[pi], s, si, p, pi+2)
        if charMatch(s, si, p, pi):
            return self.match(s, si+1, p, pi+1)
        return False

    def real_pattern(self, p):
        index = 0
        real_pattern_list = []
        prev_glob_char = None

        while index < len(p):
            if index+1 < len(p) and p[index+1] == '*':
                if prev_glob_char != p[index]:
                    prev_glob_char = p[index]
                    real_pattern_list.append(p[index:index+2])
                index += 2
            else:
                prev_glob_char = None
                real_pattern_list.append(p[index])
                index += 1

        return ''.join(real_pattern_list)

    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        return self.match(s, 0, self.real_pattern(p), 0)
