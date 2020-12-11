#!/usr/bin/env python3

from collections import *
from functools import lru_cache
import heapq
import itertools
import math
import random
import sys

def main():
    # fin = open("example", "r")
    fin = open("input", "r")
    nums = [int(line.strip()) for line in fin.readlines() if line.strip()]
    nums.sort()

    nums = [0] + nums + [nums[-1] + 3]

    last = 0
    a, b = 0, 0
    for num in nums:
        assert num - last <= 3
        if num - last == 1:
            a += 1
        elif num - last == 3:
            b += 1
        last = num
    print("part 1", a, b, a * b)

    dp = [1]
    for i in range(1, len(nums)):
        ans = 0
        for j in range(i):
            if nums[j] + 3 >= nums[i]:
                ans += dp[j]
        dp.append(ans)

    print("part 2", dp[-1])

if __name__ == "__main__":
    main()