class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        s , ans = 0, 0
        for i in gain:
            s += i
            if s > ans:
                ans = s
        return ans