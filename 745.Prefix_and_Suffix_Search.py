# Time:
 # __init__: O(WK**3), W = len(words), K = max(map(len, words))
 # f: O(1)
# Space: # O(K**2)

class WordFilter:
    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.prefix_suffix = {}
        for weight, word in enumerate(words):
            for i in range(len(word)+1):
                prefix = word[:i]
                for j in range(len(word)+1):
                    self.prefix_suffix[(prefix, word[j:])] = weight


    def f(self, prefix, suffix):
        """
        :type prefix: str
        :type suffix: str
        :rtype: int
        """
        return self.prefix_suffix.get((prefix, suffix), -1)



# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)
wf = WordFilter(['apple', 'gge', 'abced'])
def test(prefix, suffix, e):
    r = wf.f(prefix, suffix)
    print(e == r, prefix, suffix, e, r)

test('a', '', 2)
test('a', 'e', 0)
test('ab', 'e', -1)
test('', 'e', 1)
test('g', 'gge', 1)
test('gg', 'gge', 1)
test('gge', 'gge', 1)
