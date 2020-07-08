# 344, leetcode
def rev_string(in_str): 
  print(in_str.reverse()) # shortest for leetcode
  # return in_str[::-1] # slicing returns a copy in reverse
 
  # generic solution:
  # start = 0
  # end = len(in_str)-1
  # while(start < end):
  #   in_str[start], in_str[end] = in_str[end], in_str[start]
  #   start, end = start + 1, end - -1

  # return in_str

# print(rev_string("hello"))

# 412, leetcode
def fizz_buzz(n):
  ans=[]
  for i in range(1, n+1):
    ans_str = ''
    if(i%3==0): ans_str+='Fizz'
    if(i%5==0): ans_str+='Buzz'
    if(not ans_str): ans_str=i
    ans.append(ans_str)
  return(ans)

ss = 'ss'

def _fizz_buzz(n): #if there are many words, use double loop
  hash = {3: 'Fizz', 5: 'Buzz', 7: 'Jazz'}
  ans = []
  for i in range(1,n+1):
    ans_str = ''
    for key in hash.keys():
      if i%key==0: ans_str+= hash[key]
    if not ans_str: ans_str = i
    ans.append(ans_str)
  return ans
# print(fizz_buzz(30))

# 136, leetcode
def single_number(nums):
  res = 0
  for num in nums:
    res ^= num
  return res

# nums = [4,1,2,1,2]
# print(single_number(nums))

# 104, leetcode
def get_depth(root):
  if not root: #base case
    return 0
  return 1 + max(get_depth(root.left), get_depth(root.right))
 

# 283, leeetcode
def move_zeroes(arr):
  count = arr.count(0)
  # [arr.remove(i) for i in arr if i==0]
  arr = [i for i in arr if i!=0]
  arr+= [0]*count
  return arr

# print(move_zeroes([0,1,0,3,12]))

# hackerrank practice
def isPresent(arr, k):
  ans = ""
  for num in arr:
      if num == k:
          ans+= "YES"
  if(ans): print("YES")
  else: print("No")

# isPresent([1,2,3,4,5], 5)

# 371, leetcode
def sum_ints(a, b):
  return sum(list([a,b]))
# print(sum_ints(3,6))


# 169, leetcode
def majorityElement(nums):
  n = len(nums) // 2
  freqs = {}
  
  for num in nums:
    if (num not in freqs):
      freqs[num] = 1
    else:
      freqs[num] += 1
  
  for freq in freqs.items():
    if (freq[1] > n): return freq[0]

# OR #
def majorityElementVote(nums):
  count = 0
  candidate = None

  for num in nums:
    if count == 0: candidate = num
    count += (1 if num==candidate else -1)

  return candidate

# print(majorityElement([1,2,3,5,6,6,6,3,3,3]))

# 13, leetcode
def romanToInt(s):
  cache = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
  ans = 0
  for i in range(len(s)-1):
    # case 2, curr smaller than next
    if(cache[s[i]] < cache[s[i+1]]):
      ans -= cache[s[i]]
    else:
      # case 3, curr bigger than next
      ans += cache[s[i]]
  
  return ans + cache[s[-1]]

# print(romanToInt('IV'))

# 101, leetcode
class Solution:
    def isSymmetric(self, root):
        if not root: return True
        return _traverse(root.left, root.right)
        
def _traverse(node1, node2):
    if node1 and node2 and node1.val == node2.val:
        return _traverse(node1.left, node2.right) and _traverse(node1.right, node2.left)
    return node1 == node2

# 118, leetcode
# def genPascal(numRows):
#   if(numRows==1): return [1]
#   arr = []

def balance_data(str_data=None): 
  import numpy as np

  arr = np.array(str_data.strip(',x[]?.!/;:').split(',')).astype(np.float)
  n = len(arr)

  print(arr)

# balance_data("[x,1.0,0.0,3.0,12.0]")


def getDistanceMetrics(arr):
    # hash map to store individual values
    cache = {}
    # recording the occurances
    for i in range(len(arr)):
        if arr[i] not in cache.keys():
          #create arr for curr element 
          cache[arr[i]] = [i]
        else: 
          # if exists, append
          cache[arr[i]].append(i)
    
    # getting the metrics
    dists = []
    for i in range(len(arr)):
      occurances = cache[arr[i]]
      abs_arr = []
      for j in range(len(occurances)):
          prev_i = cache[arr[i]]
          # omit duplicates and single occs
          if(i!=prev_i[j] or len(occurances) < 2):
            abs_arr.append(abs(i - prev_i[j]))
      dists.append(sum(abs_arr))
    print(arr)
    print(cache)
    return dists  

# print(getDistanceMetrics([1,2,2,1,5,1]))

# 26, leetcode
def removeDuplicates(nums):
  if(len(nums) < 2): return nums
  n = 0
  for i in range(len(nums)-1):
    if(nums[i] != nums[n]):
      n += 1
      nums[n] = nums[i]
  return n
# print(removeDuplicates([1,2,2,1,5,1]))

# 122, leetcode
def buy_sell(prices):
  return