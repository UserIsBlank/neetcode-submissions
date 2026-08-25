class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # sliding window (start right after left)
        l, r = 0, 1
        stonk = 0
        while r < len(prices):
            stonk = max(stonk, prices[r] - prices[l])
            if prices[l] > prices[r]:
                l += 1
            else:
                r += 1
        return stonk
            
            
            