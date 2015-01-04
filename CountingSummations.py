# problem 76
class Count:
  def __init__(self):
    self.cache = {}

  def memoSearch(self, target, maxCoin):
    if (target, maxCoin) in self.cache:
      return self.cache[(target, maxCoin)]
    if target == 0:
      return 1
    if maxCoin < 1:
      return 0
    if maxCoin > target:
      self.cache[(target, maxCoin)] = self.memoSearch(target, maxCoin - 1)
    else:
      self.cache[(target, maxCoin)] = self.memoSearch(target - maxCoin, maxCoin) \
        + self.memoSearch(target, maxCoin - 1)
    return self.cache[(target, maxCoin)]

  def count(self, target, maxCoin):
    return self.memoSearch(target, maxCoin)

  def count_another_verison(self, target):
    ways = [1] + [0] * target
    for coin in range(1, target):
      for t in range(coin, target + 1):
        ways[t] += ways[t - coin]
    return ways[target]

sol = Count()
print sol.count(100, 99)
print sol.count_another_verison(100)

