def newton_sqrt(k):
  n = k / 2
  for _ in range(10):
    n = n - ((n**2 - k)/(2 * n))
  return n

