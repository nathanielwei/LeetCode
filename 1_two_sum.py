# smaple code by LeetCode
from typing import Any, Dict, List, Tuple, Union
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        for i, val in enumerate(nums):
            diff = target - val
            
            if val in hash:
                return [hash[val], i]
            hash[diff] = i

        return None
            


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        flag = False
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i]+nums[j] == target:
                    flag = True
                    return [i,j]
