def notes():
  pass
  # For recursion:
  #   1 define base case
  #   2 identify recursive case
  #   3 get closer to base case
  # In binary trees leaves can have 0, 1 or 2 children
  # Perfect binary trees have leaves with exactly two children
  # The number of nodes in the last layer equals the sum of all other nodes + 1:
  #         ( )
  #     ( )     ( )
  # Number of noeds = 2^h - 1
  # 
  # Full trees can have 0 or 2 children
  # 
  # Binary Search Tree(BST)
  #     10
  #    /  \
  #   1   15
  #  / \  / \
  # 0  5 11 16
  # 
  # BSTs preserve the relationship between nodes
  # BSTs: all right children must be greater than current node
  # 
  # Unbalanced BSTs have 0(N) for most operations
  # 
  # For removal of nodes:
  # 3 cases:
  # 1: Delete node with no children
  # 2: Delete node with 1 child
  # 3: Delete node with 2 children
  # BSTs have at most 2 children
  # 
  #  
  # TREE SEARCHING
  # For breadth-first search, traversal is like reading a book -- line by line:
  #      1
  #    /  \
  #   2    3
  #  /\    /\
  # 4  5  6  7
class Node:
  def __init__(self, value=None):
    self.parent = None
    self.left = None
    self.right = None
    self.value = value

from collections import deque
class BST:
  def __init__(self):
    self.root = None

  def print_tree(self):
    if self.root != None:
      self._print_tree(self.root)
  def _print_tree(self, curr):
    if curr != None:
      self._print_tree(curr.left)
      print(curr.value)
      self._print_tree(curr.right)

  def insert(self, value):
    # set new node as root if tree is empty
    if self.root == None: self.root = Node(value)
    else: self._insert(self.root, value)
  # helper to decide how far to traverse tree
  def _insert(self, curr, value):
    if value <= curr.value:
      if curr.left == None: 
        curr.left = Node(value)
        curr.left.parent = curr
      else: 
        self._insert(curr.left, value)
    else:
      if curr.right == None: 
        curr.right = Node(value)
        curr.right.parent = curr
      else: 
        self._insert(curr.right, value)

  def search(self, value): 
    if self.root:
      return self._search(self.root, value)
  def _search(self, curr, value):
    if value == curr.value: return True
    if value < curr.value and curr.left: 
      return self._search(curr.left, value)
    if value > curr.value and curr.right: 
      return self._search(curr.right, value)
    return False

  def find(self, value): 
    if self.root:
      return self._find(self.root, value)
  def _find(self, curr, value):
    if value == curr.value: return curr
    if value < curr.value and curr.left: 
      return self._find(curr.left, value)
    if value > curr.value and curr.right: 
      return self._find(curr.right, value)
    return False

  # return num children
  def num_children(self, node):
    num_children = 0
    if node.left: num_children += 1
    if node.right: num_children += 1
    return self.num_children

  def delete_value(self, value):
    return self.delete_node(self.find(value))
  def delete_node(self, node):
    # returns node with min value in tree with curr node as root
    def min_value_node(n):
      curr = n
      while curr.left:
        curr = curr.left
      return curr
    
    node_parent = node.parent
    node_children = self.num_children(node)

    # breakdown into the 3 possible cases
    # CASE 1: No children
    if node_children == 0: 
      if node_parent.left == node:
        node_parent.left = None
      else:
        node_parent.right = None
    # CASE 2: 1 child
    if node_children == 1:
      if node.left:
        child = node.left
      else:
        child = node.right
      # swap delete target with its child
      if node_parent.left == node:
        node_parent.left = child
      else:
        node_parent.right = child

      child.parent = node_parent
    # CASE 3: 2 children
    if node_children == 2:
      # select successor, the next node bigger than curr
      successor = min_value_node(node.right)
      # swap the two nodes
      node.value = successor.value
      self.delete_node(successor)

  def remove(self, value):
    # checking if root and value exist
    if self.root and self.search(value):
      return self._remove(self.root,value)
  def _remove(self, curr, value):
    if value == curr.value: 
      print("swap smallest on the right side right")
    if value == curr.right.value: curr.right = None
    if value == curr.left.value:  curr.left = None
    if value < curr.value and curr.left: 
      if(value < curr.left.value): return self._remove(curr.left, value)
      else: return self._remove(curr.left, value)
    if value > curr.value and curr.right: 
      if value > curr.right.value: return self._remove(curr.right, value)
      else: return self._remove(curr.right, value)
    return False 

  def BFS(self):
    if self.root:
      queue = deque()
      queue.append(self.root)
      result = ""
      while len(queue) > 0:
        node = queue[0]
        result += str(str(node.value) + ' ')
        queue.popleft()
        if node.left:
          queue.append(node.left)
        if node.right:
          queue.append(node.right)
      return result

  def DFS(self):
    if not self.root:
      return

  def preOrder(self):
    return traversePreOrder(self.root, [])
  def inOrder(self):
    return traverseInOrder(self.root, [])
  def postOrder(self):
    return traversePostOrder(self.root, [])

def traverseInOrder(node, list):
  if(node.left):
    traverseInOrder(node.left, list)
  list.append(node.value) ####
  
  if(node.right):
    traverseInOrder(node.right, list)
  
  return list

def traversePreOrder(node, list):
  list.append(node.value) ####

  if(node.left):
    traversePreOrder(node.left, list)
  
  if(node.right):
    traversePreOrder(node.right, list)
  
  return list  

def traversePostOrder(node, list):
  if(node.left):
    traversePostOrder(node.left, list)
  
  if(node.right):
    traversePostOrder(node.right, list)
  
  list.append(node.value)####

  return list  
  
tree = BST()

nodes = [10, 1, 0, 5, 15, 11, 16]
for node in nodes: tree.insert(node)

# tree.print_tree()
# print(tree.BFS())
#     10
#    /  \
#   1   15
#  / \  / \
# 0  5 11 16