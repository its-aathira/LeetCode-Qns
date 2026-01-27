class Solution:
    def maxProfit(self,prices):
        minPrice=float('inf')
        maxProfit=0

        for price in prices:
            if price<minPrice:
                minPrice=price
            else:
                profit=price-minPrice
                maxProfit=max(profit,maxProfit)
        return maxProfit