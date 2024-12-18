from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        d = deque()
        for i in range(len(nums)):
            if d and d[0] < i - k + 1:
                d.popleft()

            while d and nums[d[-1]] < nums[i]:
                d.pop()
            d.append(i)
            if i >= k - 1:
                result.append(nums[d[0]])

        return result
