# LC 121 Best time to buy and sell stocks

# Time complexity: O(n)
# Space complexity: O(1)


def max_profit(prices):
    left = 0
    maximum_profit = 0
    
    for right in range(1,len(prices)):
        if prices[right] < prices[left]:
            left = right
        else:
            profit = prices[right] - prices[left]
            if profit > maximum_profit:
                maximum_profit = profit

    return maximum_profit
        


print(max_profit([7, 3, 5, 1, 6]))
print(max_profit([7, 6, 4, 3, 1]))
print(max_profit([1, 2]))