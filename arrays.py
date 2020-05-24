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

def two_sum(arr, target):
    if(not arr or type(target)!=int): return False
    
    # for i in enumerate(arr):
    #     for j in enumerate(arr):
    #         if(arr[i] + arr[j] == target): return i, j
    hash = {}
    for i, n in enumerate(arr):
        # looking for the complement
        if target-n in hash: return [hash[target-n], i]
        # if not found add
        else: hash[n] = i

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
    # assumptions: in-line, w/o array copy
    for i in arr:
        pass



def main():
    # rev_for('my name is')
    # rev_slice('hi my name is')
    
    sorted1 =     [0,3,4,31,32]
    sorted2 =     [4,6,30]
    two_sum_arr = [2,7,11,15]
    max_sub_arr = [-2,1,-3,4,-1,2,1,-5,4]
    in_line_arr = [0,1,0,3,12]
    
    target = 9

    # print(mergeSorted(arr1, arr2))
    # print(two_sum(two_sum_arr, target))
    print(max_sub_sum(max_sub_arr))

main()
