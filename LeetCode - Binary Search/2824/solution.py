from typing import List

class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        length = len(nums)
        cnt = 0
        for i in range(length):
            for j in range(i+1, length):
                if nums[i] + nums[j] < target:
                    cnt += 1
        return cnt
