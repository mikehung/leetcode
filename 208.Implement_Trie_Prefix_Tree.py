#!/usr/bin/env python

class TrieNode(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s = {}
        self.isWord = False


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
            if w not in node.s:
                node.s[w] = TrieNode()
            node = node.s[w]
        node.isWord = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self.root
        for w in word:
            if w not in node.s:
                return False
            node = node.s[w]

        return node.isWord

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie
        that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node = self.root
        for w in prefix:
            if w not in node.s:
                return False
            node = node.s[w]

        return True

    def traverse(self, node, word=''):
        keys = node.s.keys()
        if not keys:
            print(word)
        for k in keys:
            self.traverse(node.s[k], word + k)


# Your Trie object will be instantiated and called as such:
trie = Trie()
trie.insert("somestring")
trie.insert("sogood")
trie.insert("goodjob")
print(trie.search("key"))
print(trie.search("somestring"))
print(trie.search("some"))
print(trie.startsWith("somestring"))
print(trie.startsWith("some"))
print(trie.startsWith("soome"))
trie.traverse(trie.root)
