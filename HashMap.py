def notes():
  '''
  - for a given array [ben:10, tim:9, leo:5, sam:12, ada:4, max:22...]
    to get the value for each key (name), instead of iterating the array 
    which can take O(n), if we already know the index of the name
    then we can simply return the value at that address. The hash code 
    is used to generate an address for the current value based on the value itself,
    so its address is related to its value. 

    https://www.youtube.com/watch?v=2Ti5yvumFTU
  '''
class Hashdata:
  def __init__(self, n):
    self.size = n if n > 0 else 1
    self.data = [None] * self.size

  def _get_hash(self, key):
    hash = 0
    for char in str(key): hash+=ord(char)
    return hash % self.size

  def add(self, key, value):
    key_index = self._get_hash(key)
    key_value_pair = [key, value]

    # if the data at the index is empty(None)
    if self.data[key_index] is None:
      self.data[key_index] = list([key_value_pair])
      return True
    else:
      for pair in self.data[key_index]:
        if pair[0] == key:
          pair[1] = value
          return True
      self.data[key_index].append(key_value_pair)
  
  def get(self, key):
    key_address = self._get_hash(key)

    if self.data[key_address] is None:
      print("Data does not exist.")
      return False
    for i in range(len(self.data[key_address])):
      if self.data[key_address][i][0] == key:
        return self.data[key_address].pop(i)
         
  
  def set(self, key, value):
    # address of key
    key_address = self._get_hash(key)

    if self.data[key_address] is None:
      print("Data does not exist.")
      return False
    else: #found the value
      for pair in self.data[key_address]:
        if pair[0] == key:
          pair[1] = value
          return True

  def get_keys(self):
    keys = []
    # double loop in case there are collisions
    for i in range(len(self.data)):
      if(self.data[i]):
        for j in range(len(self.data[i])):
          keys.append(self.data[i][j][0])
    return keys

ss = Hashdata(1)
ss.add('bob', 22)
ss.add('salmon', 23)
ss.add('tuna', 2000)
ss.add('solomon', 512)
ss.add('pisa', 2020)
ss.add('pi2a', 2020)
ss.add('pi1a', 2020)
ss.add('pifa', 2020)
ss.add('pi22a', 2020)
ss.add('pikasf', 2020)
# print(ss.get('tuna'))
print("data", ss.data)
print("keys", ss.get_keys())

