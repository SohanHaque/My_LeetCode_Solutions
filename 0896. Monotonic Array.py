class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        checking = 0
        flag = 0
        length = len(nums)
        
        for i in range(length - 1):
            if nums[i] == nums[i + 1]:
                continue
            elif nums[i] < nums[i + 1]:
                if checking == 0 or checking == 1:
                    checking = 1
                    flag = -1
                else:
                    return False
            elif nums[i] > nums[i + 1]:
                if checking == 0 or checking == -1:
                    checking = -1
                    flag = -1
                else:
                    return False
        
        if (nums[0] == nums[length-1]) and flag == 0:
            return True

        return checking != 0
            
        