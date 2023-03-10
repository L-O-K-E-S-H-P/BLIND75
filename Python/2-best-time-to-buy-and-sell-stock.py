class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buying=prices[0]
        profit=0
        for i in range(1,len(prices)):
            if prices[i]<buying:
                buying=prices[i]
            else:
                profit=max(profit,prices[i]-buying)
        return profit
