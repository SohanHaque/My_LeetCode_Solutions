class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        a=0
        b=0
        i=1
        while i<len(colors)-1:
            if colors[i-1:i+2] == "AAA":
                a+=1
            elif colors[i-1:i+2] == "BBB":
                b+=1
            i+=1
        
        return a > b