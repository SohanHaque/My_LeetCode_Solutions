class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n+1)
        for i in range(1, n+1):
            count = 0
            num = i
            while num:
                num &= (num-1)
                count += 1
            ans[i] = count
        return ans