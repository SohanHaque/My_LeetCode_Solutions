class Solution:
    def numOfArrays(self, n, m, k):
        if m < k: return 0
        ans = [[1] * m] + [[0] * m for _ in range(k - 1)]
        t = 10 ** 9 + 7
        for _ in range(n - 1):
            for i in range(k - 1, -1, -1):
                count = 0
                for j in range(m):
                    ans[i][j] = (ans[i][j] * (j + 1) + count) % t
                    if i: count = (count + ans[i - 1][j]) % t
        return sum(ans[-1]) % t
