class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_so_far, max_profit = prices[0], 0
        for i in prices:
            if i < min_so_far:
                min_so_far = i
            elif (i - min_so_far) > max_profit:
                max_profit = i - min_so_far
        return max_profit
