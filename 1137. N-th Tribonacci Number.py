class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0: return 0
        elif n < 2: return 1
        else:
            n1, n2, n3 = 0, 1, 1
            for i in range(n-2):
                n1, n2, n3 = n2, n3, n1+n2+n3
        return n3