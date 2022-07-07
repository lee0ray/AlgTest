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


class KMP:
    def __init__(self, pat=''):
        self.pat = pat
        m = len(pat)
        self.dp = [[0] * 256 for _ in range(m)]

        # base case
        self.dp[0][ord(pat[0])] = 1
        x = 0
        for j in range(1, m):
            print(x,j)
            for k in range(256):
                self.dp[j][k] = self.dp[x][k]

            self.dp[j][ord(pat[j])] = j + 1
            x = self.dp[x][ord(pat[j])]
            print(x)
        print(self.dp)

    def search(self, txt: str):
        m = len(self.pat)
        n = len(txt)
        j = 0
        for i in range(n):
            j = self.dp[j][ord(txt[i])]
            if j == m:
                return i - m + 1

        return -1


if __name__ == '__main__':
    t = KMP("ababefc")
    print(t.search("123456ababc"))
    pass
