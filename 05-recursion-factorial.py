# 1 define base case
# 2 identify recursive case
# 3 get closer to base case

def recursiveFactorial(input_num):
  if(input_num == 2): return 2
  return(input_num * recursiveFactorial(input_num-1))

def iterativeFactorial(input_num):
  ans = 1
  while input_num > 0:
    ans*=input_num
    input_num-=1
  return(ans)
  
print(recursiveFactorial(5))
  
# 5! = 5*4*3*2*1
# base case 0
# exit if i < 1
# total = 0
# curr = 4
# total = total + (total*curr-1)
iterativeFactorial(3) 