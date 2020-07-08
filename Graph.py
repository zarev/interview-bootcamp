class Node:
  def __init__(self, data=None):
    self.data = data
    self.prev = None
    self.next = None

class Graph():
  def __init__(self):
    self.nodes = 0
    self.adjacentList = {}

  def addNode(self, node):
    self.adjacentList[node] = []
    self.nodes+=1
  
  def addEdge(self, node1, node2):
    self.adjacentList[node1].push(node2)
    self.adjacentList[node2].push(node1)

  