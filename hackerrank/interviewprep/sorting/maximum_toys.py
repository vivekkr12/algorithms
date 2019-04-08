def maximum_toys(prices, k):
    count_toys = 0
    total_price = 0
    prices.sort()
    n = len(prices)

    for i in range(n):
        if total_price + prices[i] <= k:
            total_price += prices[i]
            count_toys += 1
        else:
            break

    return count_toys


if __name__ == '__main__':
    max_toys = maximum_toys([3, 7, 2, 9, 4], 15)
    print(max_toys)
