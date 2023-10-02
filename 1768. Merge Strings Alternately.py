class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        t = len(word1) + len(word2)
        ans = ""
        if word1 == "":
            return word2
        elif word2 == "":
            return word1
        
        for i in range(t):
            if i % 2 == 0 and i//2 < len(word1):
                ans += word1[i//2]
            elif i % 2 != 0 and i//2 < len(word2):
                ans += word2[i//2]
            elif i//2 >= len(word1) :
                ans += word2[(i//2) :]
                return ans
            else:
                ans += word1[(i//2)+1 :]
                return ans

        return ans