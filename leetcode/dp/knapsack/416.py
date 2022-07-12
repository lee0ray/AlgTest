import heapq
import collections
import math
from collections import Counter
from collections import deque
from collections import defaultdict
from typing import List
import time


class SolutionOld:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        n = len(nums)
        if s % 2 != 0:
            return False

        target = int(s / 2)
        # dp[i][j] 前i个数 中能否 和为j
        dp = [[False] * (target + 1) for _ in range(n)]

        for i in range(n):
            for j in range(target + 1):
                if j == 0:
                    dp[i][j] = True

        # dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i]]
        for i in range(n):
            for j in range(target + 1):
                if nums[i] == target:
                    return True
                if j - nums[i] >= 0:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i]]
                else:
                    dp[i][j] = dp[i - 1][j]
        print(dp)

        return dp[-1][-1]


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        n = len(nums)
        if s % 2 != 0:
            return False

        target = int(s / 2)
        # dp[i][j] 前i个数 中能否 和为j
        dp = [False] * (target + 1)

        dp[0] = True

        # dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i]]
        for i in range(n):
            dpNew = [False] * (target + 1)
            for j in range(target + 1):
                if nums[i] == target:
                    return True
                if j - nums[i] >= 0:
                    dpNew[j] = dp[j] or dp[j - nums[i]]
                else:
                    dpNew[j] = dp[j]
            dp = dpNew
        print(dp)

        return dp[-1]


if __name__ == '__main__':
    s = Solution()
    print(s.canPartition([1, 2, 3, 5]))
    pass
