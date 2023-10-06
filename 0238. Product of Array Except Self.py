class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        count, n = 1, len(nums)
        ans = [1] * n
        for i in range(n):
            ans[i] = ans[i]*count
            count = count*nums[i]
        count = 1
        for i in range(n-1, -1, -1):
            ans[i] = ans[i]*count
            count = count*nums[i]
        return ans