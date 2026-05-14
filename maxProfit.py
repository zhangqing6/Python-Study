class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_profit=float("inf")
        max_profit=0
        for price in prices:
            if min_profit>price:
                min_profit=price
            else:
                max_profit=max(max_profit,price-min_profit)
        return max_profit
