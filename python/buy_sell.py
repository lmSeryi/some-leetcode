def buy_sell(prices):
    profit = 0
    min_price = prices[0]

    for price in prices:
        profit = max(profit, price - min_price)
        min_price = min(min_price, price)

    return profit

print(buy_sell([7,5,3,1,6,4]))