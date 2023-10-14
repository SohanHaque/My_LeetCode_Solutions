# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        f = 1
        while f <= n:
            mid = f+(n-f)//2
            temp = guess(mid)
            if temp == -1:
                n = mid-1
            elif temp == 1:
                f = mid+1
            else:
                return mid
        return mid