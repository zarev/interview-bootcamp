def bubble(arr):
  for i in range(0, len(arr)-1):
    for j in range(0, len(arr)-1): 
      # print(arr[num], arr[num-1])
      if(arr[j] >  arr[j + 1]): 
        # swap 
        tmp = arr[j]
        arr[j] = arr[j + 1]
        arr[j + 1] = tmp

  print(arr)

def selection(arr):
  for i in range(len(arr)-1):
    smallest_index = i
    for j in range(i+1, len(arr)):
      # print(arr[j])
      if(arr[j] < arr[smallest_index]):
        smallest_index = j
      # swap
    tmp = arr[i]
    arr[i] = arr[smallest_index]
    arr[smallest_index] = tmp   
    print(arr)


def insertion(arr):
  for i in range(1,len(arr)):
    #element to be compared
    current = arr[i]
    #comparing the current element with the sorted portion and swapping
    while i>0 and arr[i-1]>current:
        arr[i] = arr[i-1]
        i -= 1
    arr[i] = current
    print(arr)

# MergeSort(arr[], l,  r)
# If r > l
#      1. Find the middle point to divide the array into two halves:  
#              middle m = (l+r)/2
#      2. Call mergeSort for first half:   
#              Call mergeSort(arr, l, m)
#      3. Call mergeSort for second half:
#              Call mergeSort(arr, m+1, r)
#      4. Merge the two halves sorted in step 2 and 3:
#              Call merge(arr, l, m, r)
def merge(arr): 
    if len(arr) >1: 
        mid = len(arr)//2 #Finding the mid of the array 
        L = arr[:mid] # Dividing the array elements  
        R = arr[mid:] # into 2 halves 
  
        merge(L) # Sorting the first half 
        merge(R) # Sorting the second half 
  
        i = j = k = 0
          
        # Copy data to temp arrays L[] and R[] 
        while i < len(L) and j < len(R): 
            if L[i] < R[j]: 
                arr[k] = L[i] 
                i+=1
            else: 
                arr[k] = R[j] 
                j+=1
            k+=1
          
        # Checking if any element was left 
        while i < len(L): 
            arr[k] = L[i] 
            i+=1
            k+=1
          
        while j < len(R): 
            arr[k] = R[j] 
            j+=1
            k+=1
def printList(arr): 
    for i in range(len(arr)):         
        print(arr[i],end=" ") 
    print() 
numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
merge(numbers)
printList(numbers)
print(sorted(numbers))