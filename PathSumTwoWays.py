def findMinPath(matrix):
  pre = []
  n = len(matrix)
  m = len(matrix[0])
  for row in range(n):
    curr = []
    for col in range(m):
      candidates = []
      val = matrix[row][col]
      if curr:
        candidates.append(val + curr[-1])
      if pre:
        candidates.append(val + pre[col])
      if candidates:
        curr.append(min(candidates))
      else:
        curr.append(val)
    pre = curr
  return curr[-1]

# print findMinPath([[131, 673, 234,103, 18],
#                   [201, 96, 342, 965, 150], 
#                   [630, 803, 746, 422, 111],
#                   [537, 699, 497, 121, 956],
#                   [805, 732, 524, 37, 331]])

f = open('p081_matrix.txt', 'r')
matrix = []
for line in f:
  matrix.append([int(x) for x in line.split(',')])
print findMinPath(matrix)