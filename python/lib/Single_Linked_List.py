# a singlely linked node
class Node:
  def __init__(self, value):
    self.value = value
    self.next = None
  def __repr__(self):
    return f'{self.value}'


class Single_Linked_List:
  def __init__(self):
    self.head = None
    self.tail = None
    self.size = -1

  # check if list has nodes
  def is_empty(self):
    return self.size == -1

  def log(self):
    current_node = self.head
    while(current_node):
      print(current_node)
      current_node = current_node.next 

  # calc len of list
  def length(self):
    i = 0
    current_node = self.head
    while(current_node):
      current_node = current_node.next
      i += 1
    return i

  def get(self, index):
    if self.is_empty():
      return None

    if index > self.size or index < 0:
      return None

    if index == 0:
      return self.head

    if index == self.size:
      return self.tail

    i = -1
    current_node = self.head
    while(i < index):
      i += 1
      current_node = current_node.next
    
    return current_node

  # add node to end of list
  def push(self, value):
    new_node = Node(value)

    if self.is_empty():
      self.head = new_node
      self.tail = new_node
    else:
      self.tail.next = new_node
      self.tail = new_node

    self.size += 1
