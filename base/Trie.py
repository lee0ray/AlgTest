import heapq
import collections
import math
from collections import Counter
from collections import deque
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Trie:
    def __init__(self):
        self.isEnd = False
        self.Next = [None] * 26

    def insert(self, word):
        node = self
        for ch in word:
            idx = ord(ch) - ord("a")
            if not node.Next[idx]:
                node.Next[idx] = Trie()
            node = node.Next[idx]
        node.isEnd = True

    def searchPrefix(self, word):
        node = self
        for ch in word:
            idx = ord(ch) - ord("a")
            if not node.Next[idx]:
                return None
            node = node.Next[idx]
        return node

    def search(self, word):
        node = self.searchPrefix(word)
        return node is not None and node.isEnd

    def startsWith(self, word):
        return self.searchPrefix(word) is not None


if __name__ == '__main__':

    t = Trie()

    t.insert("app")

    print(t.search("a"))
    print(t.search("apple"))
    print(t.startsWith("app"))
    print(t.startsWith("b"))