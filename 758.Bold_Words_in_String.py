class Solution:
    def boldWords(self, words, S):
        """
        :type words: List[str]
        :type S: str
        :rtype: str
        """
        bold = [False] * len(S)
        for word in words:
            idx = S.find(word)
            while idx != -1:
                for i in range(len(word)):
                    bold[idx+i] = True
                idx = S.find(word, idx+1)

        ans = []
        i = 0
        while i < len(S):
            if bold[i]:
                ans += '<b>'
                while i < len(S) and bold[i]:
                    ans.append(S[i])
                    i += 1
                ans += '</b>'
            else:
                ans.append(S[i])
                i += 1

        return ''.join(ans)


S = 'aabcabc'
words = ['ab', 'cd']
print(S, words)
print(Solution().boldWords(words, S))

S = "aabcd"
words = ['ab', 'bc', 'abc']
print(S, words)
print(Solution().boldWords(words, S))

S = "aabcd"
words = ['aa', 'cd']
print(S, words)
print(Solution().boldWords(words, S))

S = 'a'
words = ['a']
print(S, words)
print(Solution().boldWords(words, S))

S = 'a'
words = ['b']
print(S, words)
print(Solution().boldWords(words, S))

S = ''
words = ['a', 'b']
print(S, words)
print(Solution().boldWords(words, S))
