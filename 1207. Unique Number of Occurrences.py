class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hmap,s = {},set()
        for i in arr:
            hmap[i]=hmap.get(i,0)+1
        for i in hmap.values():
            if i in s: return False
            s.add(i)
        return True