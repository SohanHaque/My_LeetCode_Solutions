class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans, p1, p2 = 0, 0, len(height)-1
        while p1 < p2:
            w = p2-p1
            h = min(height[p1],height[p2])
            ans = max(ans, w*h)

            if height[p1] < height[p2]:
                p1+=1
            else:
                p2-=1
        
        return ans