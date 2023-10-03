class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if len(flowerbed) == 2 and flowerbed[1] == 0  and flowerbed[0] == 0: return n < 2
        elif len(flowerbed) == 1 and flowerbed[0] == 0: return n < 2
        ans = 0
        if flowerbed[0] == 0 and flowerbed[1] == 0:
            ans+=1
            flowerbed[0] = 1
        if flowerbed[-1] == 0 and flowerbed[-2] == 0:
            ans+=1
            flowerbed[-1] = 1
        for i in range(1, len(flowerbed)-1):
            if flowerbed[i-1] == 0 and flowerbed[i] == 0 and flowerbed[i+1] == 0:
                ans+=1
                flowerbed[i] = 1
        
        return n <= ans