#!/usr/bin/env python2

class TrieNode(object):
    def __init__(self):
        self.words= {}
        self.isWord = False

    def containChar(self, c):
        return c in self.words

    def addChar(self, c):
        if self.containChar(c):
            return
        self.words[c] = TrieNode()

    def getChar(self, c):
        if not self.containChar(c):
            return
        return self.words[c]

    def getKeys(self):
        return self.words.keys()

class WordDictionary(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        node = self.root
        for c in word:
            node.addChar(c)
            node = node.getChar(c)
        node.isWord = True

    def searchForRoot(self, root, word):
        node = root
        for i, c in enumerate(word):
            if c == '.':
                for key in node.getKeys():
                    if self.searchForRoot(node.getChar(key), word[i+1:]):
                        return True
                return False

            if not node.containChar(c):
                return False
            node = node.getChar(c)

        return node.isWord

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could
        contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        child_nodes = [self.root]

        for c in word:
            nodes = child_nodes
            child_nodes = []

            if not nodes:
                break

            for node in nodes:
                if c == '.':
                    child_nodes += node.words.values()
                elif node.containChar(c):
                    child_nodes.append(node.getChar(c))

        return any([node.isWord for node in child_nodes])


# Your WordDictionary object will be instantiated and called as such:
wordDictionary = WordDictionary()
# wordDictionary.addWord("word")
# print(wordDictionary.search("pattern"))
# print(wordDictionary.search("word"))
# print(wordDictionary.search("wo.d"))
# print(wordDictionary.search("wo.x"))
# wordDictionary.addWord("worx")
# print(wordDictionary.search("wo.x"))
# wordDictionary.addWord("at")
# wordDictionary.addWord("and")
# wordDictionary.addWord("an")
# wordDictionary.addWord("add")
# print(wordDictionary.search("a"))
# print(wordDictionary.search(".at"))
# wordDictionary.addWord("bat")
# print(wordDictionary.search(".at"))
# print(wordDictionary.search("an."))
# print(wordDictionary.search("a.d."))
# print(wordDictionary.search("b."))
# print(wordDictionary.search("a.d"))
# print(wordDictionary.search("."))
# [false,false,true,true,false,false,true,false]
wordDictionary.addWord("ran")
wordDictionary.addWord("rune")
wordDictionary.addWord("runner")
wordDictionary.addWord("runs")
wordDictionary.addWord("add")
wordDictionary.addWord("adds")
wordDictionary.addWord("adder")
wordDictionary.addWord("addee")
a = []
a.append(wordDictionary.search("r.n"))
a.append(wordDictionary.search("ru.n.e"))
a.append(wordDictionary.search("add"))
a.append(wordDictionary.search("add."))
a.append(wordDictionary.search("adde."))
a.append(wordDictionary.search(".an."))
a.append(wordDictionary.search("...s"))
a.append(wordDictionary.search("....e."))
a.append(wordDictionary.search("......."))
a.append(wordDictionary.search("..n.r"))
print(a)
