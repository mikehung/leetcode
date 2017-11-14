#!/usr/bin/env python
# Time: O(n), n = len(formula)
# Space: O(n)

class Solution(object):
    def countOfAtoms(self, formula):
        """
        :type formula: str
        :rtype: str
        """
        def add(ret, atom, num):
            if atom is None:
                return
            if num is None:
                num = 1

            atom = ''.join(atom)
            if atom in ret:
                ret[atom] += num
            else:
                ret[atom] = num


        def merge(ret, r):
            for atom, num in r.items():
                if atom in ret:
                    ret[atom] += num
                else:
                    ret[atom] = num


        def multiply(ret, n):
            if n is None:
                return

            for atom, num in ret.items():
                ret[atom] = num*n


        def count(formula, idx):
            ret = {}
            atom, num = None, None

            while idx < len(formula):
                if formula[idx] == '(':
                    add(ret, atom, num)
                    atom, num = None, None

                    r, idx = count(formula, idx+1)
                    merge(ret, r)
                elif formula[idx].isupper():
                    add(ret, atom, num)
                    atom, num = [formula[idx]], None
                elif formula[idx].islower():
                    atom.append(formula[idx])
                elif formula[idx].isdigit():
                    if num is None:
                        num = int(formula[idx])
                    else:
                        num = num*10 + int(formula[idx])
                elif formula[idx] == ')':
                    add(ret, atom, num)
                    atom, num = None, None

                    n = None
                    while idx+1 < len(formula) and formula[idx+1].isdigit():
                        if n is None:
                            n = int(formula[idx+1])
                        else:
                            n = n*10 + int(formula[idx+1])
                        idx += 1
                    multiply(ret, n)
                    return ret, idx
                idx += 1

            add(ret, atom, num)
            return ret, idx

        c, _ = count(formula, 0)
        ret = []
        for atom in sorted(c.keys()):
            ret.append(atom)
            if c[atom] != 1:
                ret.append(str(c[atom]))

        return ''.join(ret)


def test(formula, e):
    r = Solution().countOfAtoms(formula)
    print(r == e, formula, e, r)


test('H2O', 'H2O')
test('H(H)2', 'H3')
test('H(HHaO)2', 'H3Ha2O2')
test('K4(ON(SO3)2)2', 'K4N2O14S4')
test('((K)14(ON((((S)))(O)13)2)2)', 'K14N2O54S4')
