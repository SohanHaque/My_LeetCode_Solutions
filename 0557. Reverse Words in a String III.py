class Solution:
    def reverseWords(self, s: str) -> str:
        temp = s.split(" ")
        rev = [i[::-1] for i in temp]
        ans = ' '.join(rev)
        return ans
