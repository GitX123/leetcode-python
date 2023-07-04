'''
No. 121
Easy
'''

from typing import List

class Solution(object):
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        price_min = float('inf')
        for i in range(len(prices)):
            if prices[i] < price_min:
                price_min = prices[i]
            else:
                max_profit = max(max_profit, prices[i] - price_min)
        return max_profit