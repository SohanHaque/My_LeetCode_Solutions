class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        
        stack = []
        t = float('-inf')
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] < t:
                return True
            while(stack and nums[i] > stack[-1]):
                t = stack.pop()
            stack.append(nums[i])
        return False