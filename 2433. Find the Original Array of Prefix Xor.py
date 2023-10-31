class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        out = [0] * len(pref)
        out[0] = pref[0]
        for i in range(1, len(pref)):
            out[i] = pref[i - 1] ^ pref[i]
        return out