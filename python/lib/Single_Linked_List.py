class Node:
  def __init__(self, value):
    self.value = value
    self.next = None


class Single_Linked_List:
  def __init__(self):
    self.head = None
    self.tail = None
    self.size = 0

  def is_empty(self):
    return self.size == 0