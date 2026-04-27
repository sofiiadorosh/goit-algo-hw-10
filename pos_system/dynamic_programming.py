def find_min_coins(change, coins):
    counts = [float('inf')] * (change + 1)
    counts[0] = 0

    picked = [0] * (change + 1)

    for amount in range(1, change + 1):
        for coin in coins:
            if amount >= coin:
                if counts[amount - coin] + 1 < counts[amount]:
                    counts[amount] = counts[amount - coin] + 1
                    picked[amount] = coin

    if counts[change] == float('inf'):
        return {}

    wallet = {}
    while change > 0:
        coin = picked[change]
        wallet[coin] = wallet.get(coin, 0) + 1
        change -= coin

    return dict(sorted(wallet.items()))


sample = [50, 25, 10, 5, 2, 1]

print(find_min_coins(113, sample))
