class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hMap = {}
        for i, j in enumerate(nums):
            a = target - j
            if a in hMap:
                return [hMap[a], i]
            hMap[j] = i
        
