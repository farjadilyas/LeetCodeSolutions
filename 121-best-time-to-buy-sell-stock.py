"""
  121. Best time to buy and sell stock

  Approach:
  - Easy
"""


def maxProfit(self, prices: List[int]) -> int:
    mn = prices[0]
    pf = 0
    for price in prices:
        if price - mn > pf:
            pf = price - mn
        pf = max(pf, price - mn)
        if price < mn:
            mn = price
    return pf
