def rev_slice(string):
    if(type(string) == str): print(string[::-1])

def rev_for(string):
    for char in range(len(string), 0, -1):
        print(string[char-1])

def mergeSorted(arr1, arr2):
    # check input
    if(len(arr1) == 0): return arr2
    if(len(arr2) == 0): return arr1

    merged = []
    i, j = 0, 0
    len1, len2 = len(arr1), len(arr2)

    # while there are 2 arrays
    while(i<len1 and j<len2):
        if(arr1[i] < arr2[j]):
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1
    # if only arr1 left
    t1,t2=0,0
    while(i < len1):
        merged.append(arr1[i])
        i += 1
    # if only arr2 left
    while(j < len2):
        merged.append(arr2[j])
        j += 1
    
    return merged



def max_sub_sum(arr):
    if(not arr): raise ValueError('Array must not be empty.')
    running_max = arr[0]
    maxses = [running_max]
    for i in range(len(arr)-1):
        nxt = arr[i+1]
        running_max = max(nxt, running_max + nxt)
        maxses.append(running_max)
    return max(maxses)
    #     maxSum = [arr[0]]*len(arr)
    #       for i in range(len(arr)-1):
    #             maxSum[i] = max( arr[i], arr[i] + maxSum[i - 1] )
    #       return max(maxSum)

def moveZeroes(arr):
    # input:  [0,1,0,3,12]
    # output: [1,3,12,0,0]
    # edge cases: 
    # asumptions: in-line, w/o array copy
    count = arr.count(0)
    # [arr.remove(i) for i in arr if i==0]
    arr = [i for i in arr if i!=0]
    arr+= [0]*count
    return arr

def containtsDuplicates(arr):
    return len(arr) > len(set(arr))

def rotate(arr, k):
    """
    Do not return anything, modify nums in-place instead.
    [-1, -100, 3, 99], k=2 

    """ 
    def reverse(arr, start, end):
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1

    lenn = len(arr)
    k = k % lenn
    # reverse the whole list
    # then each side of k
    reverse(arr, 0, lenn-1)
    reverse(arr, 0, k - 1)
    reverse(arr, k, lenn-1)
 
def first_reccuring(arr): 
    hash = {}
    for n in arr:
        if n in hash: return n
        # if not found add to hash
        else: hash[n] = n

def main():
    # rev_for('my name is')
    # rev_slice('hi my name is')
    # arr =         [0,1,2,3]
    # k = 3
    # for i in range(len(arr)):
    #     new_i = (i+k) % len(arr)

    # sorted1 =     [0,3,4,31,32]
    # sorted2 =     [4,6,30]
    # two_sum_arr = [2,7,11,15]
    # max_sub_arr = [-2,1,-3,4,-1,2,1,-5,4]
    # in_line_arr = [0,1,0,3,12]
    # arr_rotate =  [-1, -100, 3, 99]
    first_reccur = [3,1,4,2,3]
    # target = 9
    # print(mergeSorted(arr1, arr2))
    # print(two_sum(two_sum_arr, target))
    # print(max_sub_sum(max_sub_arr))
    # print(moveZeroes(in_line_arr))
    # print(containtsDuplicates([3,3]))
    # print(len(sorted1) > len(set([1,1])))
    # print(rotate(arr_rotate,2))
    print(first_reccuring(first_reccur))
    # [start:stop:step] 



main()
