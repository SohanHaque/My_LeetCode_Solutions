class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return (sum(nums) - 2 * sum(set(nums))) * -1
