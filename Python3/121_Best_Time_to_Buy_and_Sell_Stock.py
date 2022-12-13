from typing import List


class Solution:
    """
    This is the brute-force solution.
    """
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        for j in range(len(prices) - 1):
            for i in range(j, len(prices)):
                tmp = prices[i] - prices[j]
                if tmp > profit:
                    profit = tmp

        return profit


class Solution:
    """
    NeetCode solution. This is more time efficient solution.
    """
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        left_pointer = 0
        right_pointer = 1

        while right_pointer < len(prices):
            if prices[left_pointer] < prices[right_pointer]:
                profit = max(profit, prices[right_pointer] - prices[left_pointer])

            else:
                left_pointer = right_pointer

            right_pointer += 1

        return profit