#!/usr/bin/env python

class TrieNode(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        # a~z is 26 char
        self.s = [None]*26
        self.c = 0

    @staticmethod
    def index(w):
        return ord(w) - ord('a')


class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        node = self.root
        for w in word:
            i = TrieNode.index(w)
            if not node.s[i]:
                node.s[i] = TrieNode()
            node = node.s[i]
        node.c += 1

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self.root
        for w in word:
            i = TrieNode.index(w)
            if not node.s[i]:
                return False
            node = node.s[i]

        return node.c > 0

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie
        that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node = self.root
        for w in prefix:
            i = TrieNode.index(w)
            if not node.s[i]:
                return False
            node = node.s[i]

        return True


# Your Trie object will be instantiated and called as such:
trie = Trie()
trie.insert("somestring")
print(trie.search("key"))
print(trie.search("somestring"))
print(trie.search("some"))
print(trie.startsWith("somestring"))
print(trie.startsWith("some"))
print(trie.startsWith("soome"))
