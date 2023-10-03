class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        ans=0
        count = {}
        for i in nums:
            if i in count:
                ans+=count[i]
                count[i]+=1
            else:
                count[i]=1
        return ans