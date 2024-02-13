class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a','e','i','o','u','A','E','I','O','U'}
        sz, count = 0, 0
        for i in range(len(s)):
            if s[i] in vowels:
                sz+=1
            if i >= k:
                if s[i-k] in vowels:
                    sz-=1
            count = max(count,sz)
        return count
