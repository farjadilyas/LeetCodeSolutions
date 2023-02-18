"""
  121. Best time to buy and sell stock

  Approach:
  - Easy
"""


def maxProfit(self, prices: List[int]) -> int:
    minimum = prices[0]
    profit = 0
    for price in prices:
        profit = max(profit, price - minimum)
        if price < minimum:
            minimum = price
    return profit
