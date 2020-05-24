arr1 = ['a', 'b', 'c', 'x']
arr2 = ['2', 'b', '2']

# nested for loop, n^2
def hasMatch(arr1, arr2):
  for i in range(len(arr1)):
    for j in range(len(arr2)):
      print(False)
      if arr1[i]==arr2[j]: 
        print(True) 
    else: break

# dictionary, n+m
# arr1 -> obj where each letter is a property
def hasMatch2(arr1, arr2):
  # loop arr1 and create object
  # dict = {}
  # for i in arr1: dict[i] = True
  # populate the dictionary with a true
  # value for each character from arr1
  dict = {char : True for char in arr1}

  # loop through second array and check if
  # item exists in the dict  
  for i in range(len(arr2)):
    # print(True) if dict.__contains__(arr2[i]) else print("")
    if (dict.__contains__(arr2[i])): 
      print(True)
      break 
  else: print(False)
  print(dict)

def hasMatch3(arr1, arr2):
  for element in arr1: print(element in arr2)

    
hasMatch3(arr1, arr2)