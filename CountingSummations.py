# problem 76
class Count:
  def __init__(self):
    self.cache = {}

  def help_count(self, n, last):
    if n < last:
      return 0
    if (n, last) in self.cache:
      return self.cache[(n, last)]
    if n == last:
      return 1
    res = 0
    for l in range(1, last + 1):
      res += self.help_count(n - last, l)
    self.cache[(n, last)] = res
    return res

  def count(self, n):
    res = 0
    for last in range(1, n):
      res += self.help_count(n, last)
    return res

sol = Count()
print sol.count(100)

