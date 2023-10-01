class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        start = 0
        dummy = {}
        for i in range(len(s)):
            if s[i] in dummy and dummy[s[i]] >= start:
                start = dummy[s[i]] + 1
        
            dummy[s[i]] = i
            ans = max(ans, i - start + 1)
        return ans    
