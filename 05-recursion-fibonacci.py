def recFib(n):
  if (n < 2): return n
  #return(recFib(n-1) + recFib(n-2))
  return(recFib(n-2) + recFib(n-1))

print(recFib(8))
