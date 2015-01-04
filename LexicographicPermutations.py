# Problem 24
class Permutation:
  def __init__(self):
    self.dic = {1:1, 0:1}
    self.res = []

  def getFactorial(self, n):
    if n not in self.dic:
      self.dic[n] = n * self.getFactorial(n - 1)
    return self.dic[n]

  def findPermutation(self, arr, numb):
    if not arr:
      return
    n = len(arr)
    firstIndex = numb / self.getFactorial(n - 1)
    self.res.append(arr[firstIndex])
    self.findPermutation(arr[: firstIndex] + arr[firstIndex + 1 :], numb % self.getFactorial(n - 1))
    return ''.join([str(x) for x in self.res])

sol = Permutation()
print sol.findPermutation([0,1,2, 3, 4, 5, 6, 7, 8, 9], 10 ** 6 - 1)

