def find_coins_greedy(change, coins):
    change_dict = {}
    coins = sorted(coins, reverse=True)

    for coin in coins:
        count = change // coin
        if count:
            change_dict[coin] = count
            change %= coin

    return change_dict


sample = [50, 25, 10, 5, 2, 1]

print(find_coins_greedy(113, sample))