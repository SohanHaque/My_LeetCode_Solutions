class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3: return False
        n1, n2 = float('inf'), float('inf')
        for i in nums:
            if i <= n1: n1 = i
            elif i <= n2: n2 = i
            else: return True
        return False