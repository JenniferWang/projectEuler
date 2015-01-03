def selfPowers(n, d):
  result = 0
  for i in range(1, n + 1):
    curr = 1
    for j in range(i):
      curr = (curr * i) % (10**d)
    result = (result + curr) % (10**d)
  print result

selfPowers(1000, 10)