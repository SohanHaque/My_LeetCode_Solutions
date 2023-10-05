class Solution:
    def reverseVowels(self, s: str) -> str:
        j, i = len(s)-1, 0
        vowel = set('AEIOUaeiou')
        s = list(s)
        while i < j:
            while i < j and s[i] not in vowel:
                i+=1
            while i < j and s[j] not in vowel:
                j-=1
            s[i], s[j] = s[j], s[i]
            i+=1
            j-=1 
        return ''.join(s)