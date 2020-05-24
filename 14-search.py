# DFS vs BFS
# For both time is O(n)

# BFS is good for finding the shortest path
# BFS needs more memory becauses it tracks the leaves
# Better if target is near the head of the tree/graph

# DFS: does the path exist? 
# Less memory, but can get slow as it touches all leaves

# if solution is close to the root use: BFS
# if tree is deep are solutions are rare: BFS
# if tree is very wide: DFS
# if solutions are frequent but located deep in tree: DFS
# if deciding if path exists: DFS
# if deciding on shortest path: BFS

# see 10-trees.py