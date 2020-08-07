# 344, leetcode
def rev_string(in_str): 
  print(in_str.reverse()) # shortest for leetcode, only works on char[]
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
  freqs = dict.fromkeys(nums, 1)
  
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

# 7, leetcode 
def rev_int(x: int) -> int:
  rev = 0
  a = abs(x)
  while(a != 0):
    rev = (rev*10) + a % 10
    a = a//10
  if(rev >= 2**31 or rev <= -2**31): return 0
    
  return rev if x >= 0 else -rev

# print(rev_int(-123))

# 387, leetcode, input string s
def firstUniquChar(s):
  cache = dict.fromkeys(s, 0)
  for ch in s: 
    cache[ch] += 1
  for key, val in cache.items():
    if val == 1: return s.index(key)
  return -1

# print(firstUniquChar('leetcode'))

# 242, leetcode, valid anagram
def validAnagram(s1, s2):
  if(s1==s2): return True
  if(len(s1) != len(s2)): return False
  # return sorted(s1) == sorted(s2)
  # OR
  # from collections import  Counter
  # return collections.Counter(s) == collections.Counter(t)
  counter = [0]*26
  for i in range(len(s1)-1):
    counter[ord(s1[i]) - ord('a')] += 1
    counter[ord(s2[i]) - ord('a')] -= 1
  
  for count in counter: 
    if(count !=0): return False
    
  return True

# print(validAnagram('anagram', 'nagaram'))

# 1, leetcode Two Sum
def two_sum(arr, target):
    if(not arr or type(target)!=int): return False
    
    # for i in enumerate(arr):
    #     for j in enumerate(arr):
    #         if(arr[i] + arr[j] == target): return i, j
    hash = {}
    for i, n in enumerate(arr):
        # looking for the complement(target-n)
        if target-n in hash: return [hash[target-n], i]
        # if not found add
        else: hash[n] = i

# print(two_sum([2,7,11,15], 9))

# 66, leetcode Plus One
def plusOne(digits):
  # # if input is [9]
  # if len(digits) == 1 and digits[0]==9: return [1,0]
  # # if last digit is not 9
  # if digits[-1] != 9:
  #   digits[-1] += 1
  #   return digits
  # # if it is 9, rollover
  # else:
  #   digits[-1] = 0
  #   digits[:-1] = plusOne(digits[:-1])
  #   return digits
  for i in range(len(digits)):
    # none of the numbers is 9
    if(digits[~i] < 9):
      digits[~i] += 1
      return digits
    # if there are 9s
    digits[~i] = 0
  return [1] + [0] * len(digits)

# print(plusOne([1,9,9]))
# post to comedy suicide
# cross post to heaven > Guy really milking it.
# cross post to funny > my head hurts
# 350, leetcode, arr interstect 2
from collections import Counter
def interstect(nums1, nums2):
  # save memory by always using the smaller arr
  if(len(nums2) < len(nums1)): nums1, nums2 = nums2, nums1
  res = []
  # counter creates dict with freqs
  freqs = Counter(nums1)
  for num in nums2:
    # if curr is in cache
    if (freqs[num] > 0):
      res.append(num)
      # decrement not to count again
      freqs[num] -= 1
  return res

def containtsDuplicates(arr):
    return len(arr) > len(set(arr))

# print(interstect([4,9,5], [9,4,9,8,4]))
# 36 leetcode, valid sudoku
# for loop
# strip each line of *
# check each line for dupls
def isValidSudoku(board):
  for i in range(9):
    print(i)
    # separate cols and rows and strip non digits
    curr_row = [int(k) for k in board[i] if k != '.']
    curr_col = [int(k[i]) for k in board if k[i] != '.'] 
    curr_box = [int(board[x][y]) for x in range(x/9, x/9+3) for y in range(y/9, y/9+3)]
    # rules
    isRowValid = len(curr_row) > len(set(curr_row))
    isColValid = len(curr_col) > len(set(curr_col))
    is3x3Valid = len(curr_box) > len(set(curr_box))
    
    # check for duplicates
    return(isRowValid and isColValid and is3x3Valid)



arr = [
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]

arr2 = [
  [".",".",".",".","5",".",".","1","."],
  [".","4",".","3",".",".",".",".","."],
  [".",".",".",".",".","3",".",".","1"],
  ["8",".",".",".",".",".",".","2","."],
  [".",".","2",".","7",".",".",".","."],
  [".","1","5",".",".",".",".",".","."],
  [".",".",".",".",".","2",".",".","."],
  [".","2",".","9",".",".",".",".","."],
  [".",".","4",".",".",".",".",".","."]
]
# print(len(arr) > len(set(arr)))
print(isValidSudoku(arr2))

# # arr2 = [[1,2,3], [4,5,6]]
# for i in range(1,len(arr2)+1):
#   if(len(arr2)%i==0):
#     print(i)
    # print([arr2[x][y] for x in range(i-1, i+3-1) for y in range(i-1, i+3-1)])

# for i in range(3):
  # for j in range(3):
