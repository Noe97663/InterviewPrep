# best time to buy/sell stock - maximize profit

## Brute force - nested loop - O(n^2), O(1)
## Sliding window - O(n), O(1)


def maxProfit(prices: list[int]) -> int:
    buy = 0
    sell = 1
    diff = 0
    while sell < len(prices):
        curr_diff = prices[sell] - prices[buy]
        if curr_diff > diff:
            diff = curr_diff
        if prices[sell] < prices[buy]:
            buy = sell
        sell += 1
    return diff
