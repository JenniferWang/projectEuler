# Problem 31
# This problem is better solved by up - bottom approach
# see problem 76
class Coin:
  def __init__(self, coins):
    self.cache = {}
    self.coins = coins

  def memoSearch(self, target, last_index):
    if (target, last_index) in self.cache:
      return self.cache[(target, last_index)]
    if target == 0:
      return 1
    if last_index < 0:
      return 0
    last_coin = self.coins[last_index]
    if last_coin > target:
      self.cache[(target, last_index)] = self.memoSearch(target, last_index - 1)
    else:
      self.cache[(target, last_index)] = self.memoSearch(target - last_coin, last_index) \
        + self.memoSearch(target, last_index - 1)
    return self.cache[(target, last_index)]

  def coinSums(self, target):
    return self.memoSearch(target, len(self.coins) - 1)


coins = [1, 2, 5, 10, 20, 50, 100, 200]
target = 200
coin = Coin(coins)
print coin.coinSums(200)


