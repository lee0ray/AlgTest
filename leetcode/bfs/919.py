import heapq
import collections
import math
from collections import Counter
from collections import deque
from collections import defaultdict
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class CBTInserter:

    def __init__(self, root: TreeNode):
        self.root = root
        q = deque()
        q.append(root)

        self.candidate = deque()
        while q:
            node = q.popleft()
            if node.left == None or node.right == None:
                self.candidate.append(node)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

    def insert(self, val: int) -> int:

        newNode = TreeNode(val)

        node = self.candidate[0]
        if node.left == None:
            node.left = newNode
        elif node.right == None:
            node.right = newNode
            self.candidate.popleft()
        self.candidate.append(newNode)

        return node.val

    def get_root(self) -> TreeNode:
        return self.root
