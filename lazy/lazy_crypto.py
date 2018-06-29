import sys 

def lazy_crypto(days, prices):
    coins = 0 
    money = 100
    coins, money = buy_coins(coins, money, 0, prices)
    for i, price in enumerate(prices[:-1]):
        future = prices[i+1]
        if price > future:
            coins, money = sell_coins(coins, money, i, prices)
        if price < future:
            coins, money = buy_coins(coins, money, i, prices)
    coins, money = sell_coins(coins, money, i+1, prices)
    return money

def buy_coins(coins, money, i, prices):
    coins_bought = min(money//prices[i], 100000)
    cost = coins_bought * prices[i]
    coins += coins_bought
    money -= cost
    return coins, money

def sell_coins(coins, money, i, prices):
    made = coins * prices[i]
    money += made
    coins = 0
    return coins, money

if __name__ == "__main__":
    inlist = []
    for line in sys.stdin.readlines():
        inlist.append(int(line.strip()))
    days = inlist[0]
    prices = inlist[1:]
    print(lazy_crypto(days, prices))