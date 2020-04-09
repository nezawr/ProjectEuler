

def count_coin(amount, coins):

    if amount == 0:
        return 1
    elif amount < 0 or coins == []:
        return 0
    return count_coin(amount, coins[:-1]) +\
        count_coin(amount - coins[-1], coins)


print(count_coin(200, [1, 2, 5, 10, 20, 50, 100, 200]))
