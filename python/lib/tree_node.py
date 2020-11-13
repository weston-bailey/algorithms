# node in the tree
class Tree_Node:
  def __init__(self, value):
    self.left = None
    self.right = None
    self.value = value
  
  # smaller values are moved left and greater values are moved right
  def insert_node(self, value):
    if self.value:
      if value < self.value:
        if self.left is None: 
          self.left = Tree_Node(value)
        else:
          self.left.insert_node(value)
      else:
        if self.right is None:
          self.right = Tree_Node(value)
        else:
          self.right.insert_node(value)
    else:
      self.value = value

  def print_values(self):
    if self.left:
      self.left.print_values()
    print(self.value)
    if self.right:
      self.right.print_values()

  def print_nodes(self):
    print('left: ', self.left)
    print('right: ', self.right)


