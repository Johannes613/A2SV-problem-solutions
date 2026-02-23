from typing import List


class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        lst = [0] * len(nums)

        for i in range(len(nums)):
            lst[i] = nums[nums[i]]
        return lst
        