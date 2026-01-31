from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hash_set1 = set()
        hash_set2 = set()
        ans = []

        for num1 in nums1:
            hash_set1.add(num1)
        for num2 in nums2:
            hash_set2.add(num2)

        for val in hash_set1:
            if val in hash_set2:
                ans.append(val)
        return ans


        
        