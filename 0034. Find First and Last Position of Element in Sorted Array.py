class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n, ans = len(nums), [-1,-1]
        if nums == []:
            return ans
        elif target in nums:
            for i in range(n):
                if nums[i] == target:
                    ans[0] = i
                    break
            for j in range(n-1, ans[0]-1, -1):
                if nums[j] == target:
                    ans[1] = j
                    break
        return ans