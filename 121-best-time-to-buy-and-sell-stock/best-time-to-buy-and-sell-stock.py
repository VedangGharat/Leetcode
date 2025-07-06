class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_p = 0
        l = 0
        for r in range(l, len(prices)):
            profit = prices[r] - prices[l]
            if prices[l] > prices[r]:
                l = r
            max_p = max(max_p, profit)
        return max_p