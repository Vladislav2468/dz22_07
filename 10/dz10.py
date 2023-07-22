import random

def min_flips(coins):
    heads_count = 0
    tails_count = 0
    for coin in coins:
        if coin == "H":      # H - герб
            heads_count += 1
        elif coin == "T":    # T - решка
            tails_count += 1
    return min(heads_count, tails_count)


coins_on_table = [random.choice(["H", "T"]) for _ in range(6)]
print(coins_on_table)
min_flips_needed = min_flips(coins_on_table)
print("Минимальное количество монеток, которые нужно перевернуть:", min_flips_needed)
