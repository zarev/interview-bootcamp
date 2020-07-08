class Node:
  def __init__(self, data=None):
    self.data = data
    self.prev = None
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None
    self.tail = None
    self.size = 0

  def prepend(self, data): 
    newNode = Node(data)
    if self.head is None: # list is empty
      self.append(newNode)
    else:
      self.head.prev = newNode
      newNode.next = self.head
      self.head = newNode
    self.size += 1      

  def append(self, data): 
    newNode = Node(data)
    if self.head is None: # list is empty
      self.head = newNode
      self.tail = newNode
    else:
      newNode.prev = self.tail
      self.tail.next = newNode
      self.tail = newNode
    self.size += 1

  def printList(self):
    curr = self.head
    arr = []
    while(curr):
      arr.append(curr.data)
      curr = curr.next
    print(arr)

  def insert(self, index, data):
    newNode = Node(data)
    
    # prepend to list if index is 0
    if index == 0:         return self.prepend(data)
    # append to end if index is bigger than list 
    if index >= self.size: return self.append(data)
      
    index_node = self._traversetoIndex(index-1)
    index_follower = index_node.next
    index_node.next = newNode
    newNode.prev = index_node
    newNode.next = index_follower
    index_follower.prev = newNode
    self.size+=1

  def _traversetoIndex(self, index):
        counter = 0
        curr = self.head
        while(counter != index):
          curr = curr.next
          counter+=1
        return curr

  def remove(self, index): 
    if index == 1: #removing head
      self.head = self.head.next
      return
    if index > self.size or index < 1 : return #index outside range

    target_node = self._traversetoIndex(index-1)
    target_prev = target_node.prev

    if(index == self.size): #removing the tail
      target_prev.next = None
      self.tail = target_prev
      return

    target_follower = target_node.next
    target_prev.next = target_follower
    target_follower.prev = target_prev
    self.size -= 1
 
  def node_remove(self, node):
    if self.head.data == node: #removing head
      self.head = self.head.next
      return
    prev = self.head
    while(prev.next.data != node):
      if(prev.next == node):
        prev = node
        return
      prev = prev.next
    prev.next = prev.next.next
    prev.next.next = None
  
  def reverse(self):
    if self.size == 1: return self.head

    prev = None
    head = self.head
    while(head):
      curr = head
      head = head.next
      curr.next = prev
      prev = curr
    return self
    

def rev_linked_list(head):
  prev = None
  while(head):
    next = head.next #save next
    head.next = prev #reversal
    prev = head # advance prev
    head = next # advance head
  return prev    

linked = LinkedList()
linked.append(1)
linked.append(2)
linked.append(3)
linked.append(4)
linked.printList()


