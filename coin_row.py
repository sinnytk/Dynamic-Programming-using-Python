def coin_row(coins, n):
    if n == 0:
        return 0
    if n == 1:
        return coins[0]
    return max(coin_row(coins, n-1), coin_row(coins, n-2) + coins[n-1])


coins = [5, 1, 2, 10, 6, 2]
print(coin_row(coins, len(coins)))
