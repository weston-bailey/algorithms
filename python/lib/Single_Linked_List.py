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

  # returns node at given index
  def get(self, index):
    if self.is_empty():
      return None

    if index > self.size or index < 0:
      return None

    if index == 0:
      return self.head

    if index == self.size:
      return self.tail

    i = 0
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

  # add node to begginning of list
  def append(self, value):
    new_node = Node(value)

    if self.is_empty(): 
      self.head = new_node
      self.tail = new_node
    else:
      new_node.next = self.head
      self.head = new_node
    
    self.size += 1
  
  # removes last node and returns it
  def pop(self):
    if self.is_empty(): return None
    # if size is zero, clear list
    if self.size == 0:
      popped = self.head
      self.head = self.tail = None
      self.size =- 1
      return popped

    current_node = self.get(self.size - 1)
    popped = current_node.next
    current_node.next = None
    self.size -= 1
    
    # if size is zero after decrementing, the list only has one node
    if self.size == 0:
      self.tail = self.head

    return popped

  # remove first node from list 
  def shift(self):
    if self.is_empty(): return None

    shifted = self.head
    self.head = self.head.next
    self.size -= 1

    if self.is_empty(): self.tail = None

    return shifted

  # removes a node at a specific index and returns it
  def remove(self, index):
    if self.is_empty(): return None
    if index < 0 or index > self.size: return None

    if index == 0: return self.shift()
    if index == self.size: return self.pop()

    current_node = self.get(index - 1)
    if current_node == None: return None

    removed = current_node.next
    current_node.next = current_node.next.next
    self.size -= 1

    return removed





