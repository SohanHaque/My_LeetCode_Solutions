class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        if n <= 1:
            return cost[0] if n == 1 else 0
        
        for i in range(2, n):
            cost[i] += min(cost[i-1], cost[i-2])

        return min(cost[-1], cost[-2])