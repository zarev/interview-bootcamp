def recStrRev(str):
  n = len(str)-1
  if(n < 1): print(str[n])
  print(recStrRev(str[n-1]))


def itStrRev(str):
  #for char in range(len(str)-1, 0, -1):
  #  print(str[char])
  print(str[::-1])

str = 'hello'
#itStrRev('yoyo mastery')
#recStrRev(str)
print(str)
print(str[-1], str[0], str[1])









