# problem 78
# If we use the same strategy => maximum recursion depth exceeded
class Count:
  def __init__(self, divisor):
    self.cache = {}
    self.divisor = divisor

  def memoSearch(self, target, maxCoin):
    if (target, maxCoin) in self.cache:
      return self.cache[(target, maxCoin)]
    if target == 0:
      return 1
    if maxCoin < 1:
      return 0
    if maxCoin > target:
      self.cache[(target, maxCoin)] = self.memoSearch(target, maxCoin - 1) % self.divisor
    else:
      self.cache[(target, maxCoin)] = (self.memoSearch(target - maxCoin, maxCoin) \
        + self.memoSearch(target, maxCoin - 1))  % self.divisor
    return self.cache[(target, maxCoin)]

  def count(self, target):
    return self.memoSearch(target, target)

sol = Count(10**4)
n = 1
while sol.count(n) != 0:
  n += 1
print n, sol.count(n)
