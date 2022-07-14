import heapq
import collections
import math
from collections import Counter
from collections import deque
from typing import List


class WordFilter:

    def __init__(self, words: List[str]):
        self.d = {}
        for i, word in enumerate(words):
            m = len(word)
            for prefixLength in range(1, m + 1):
                for suffixLength in range(1, m + 1):
                    self.d[word[:prefixLength] + '#' + word[-suffixLength:]] = i

    def f(self, pref: str, suff: str) -> int:
        return self.d.get(pref + '#' + suff, -1)

# class WordFilter:

#     def __init__(self, words: List[str]):
#         self.t1 = Trie()
#         self.t2 = Trie()
#         n = len(words)
#         for i in range(n):
#             w = words[i]
#             wr = w[::-1]
#             self.t1.insert(w,i)
#             self.t2.insert(wr,i)

#     def f(self, pref: str, suff: str) -> int:
#         l1 = self.t1.startWithList(pref)
#         l2 = self.t2.startWithList(suff[::-1])
#         # print(l1,l2)
#         for i in l1[::-1]:
#             for j in l2[::-1]:
#                 if i == j:
#                     return i
#         return -1

# class Trie:
#     def __init__(self):
#         self.next = [None] * 26
#         self.idxList = []

#     def insert(self,word,idx):
#         node = self
#         for ch in word:
#             i = ord(ch) - ord('a')
#             if node.next[i] is None:
#                 node.next[i] = Trie()
#             node = node.next[i]
#             node.idxList.append(idx)

#     def startWithList(self,word):
#         node = self
#         for ch in word:
#             i = ord(ch) - ord('a')
#             if node.next[i] is None:
#                 return []
#             node = node.next[i]
#         return node.idxList
