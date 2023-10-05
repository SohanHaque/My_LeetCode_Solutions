class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if nums == []:
            return []
        
        track = {}
        ans = []
        for i in nums:
            if i in track:
                track[i]+=1
            else:
                track[i]=1

        for j,k in track.items():
            if k > len(nums)//3:
                ans.append(j)
        return ans