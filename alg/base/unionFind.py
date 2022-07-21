import heapq
import collections
import math
from collections import Counter
from collections import deque
from typing import List


class UF:
    def __init__(self, n):
        self._count = n
        self.parent = [i for i in range(n)]
        self.size = [1] * n
        pass

    def find(self, p):
        while self.parent[p] != p:
            # 路径压缩
            self.parent[p] = self.parent[self.parent[p]]
            p = self.parent[p]

        return p

    def connected(self, p, q):
        rp = self.find(p)
        rq = self.find(q)
        return rp == rq

    def union(self, p, q):
        rp = self.find(p)
        rq = self.find(q)
        if rp == rq:
            return

        if self.size[rp] >= self.size[rq]:
            self.parent[rq] = rp
            self.size[rp] += self.size[rq]
        else:
            self.parent[rp] = rq
            self.size[rq] += self.size[rp]

        self._count -= 1

    def count(self):
        return self._count


if __name__ == '__main__':
    u = UF(5)
    print(u.count())
    print(u.find(0))
    print(u.connected(0, 1))
    print(u.union(0,1))
    print(u.connected(0,1))
    print(u.find(0))
    print(u.find(1))
    print(u.count())
    pass
