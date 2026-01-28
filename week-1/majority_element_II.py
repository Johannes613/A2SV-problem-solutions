from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        one_third = len(nums) / 3
        dictionary = {}
        list = []

        for num in nums:
            if num in dictionary:
                dictionary[num] += 1
            else:
                dictionary[num] = 1
        for num in dictionary:
            if dictionary[num] > one_third:
                list.append(num)
        return list
