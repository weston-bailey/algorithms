# utility namespace
from lib.float_to_str import float_to_str

class Util:
  pass

util = Util()
util.float_to_str = float_to_str

# for data to be sorted
from lib.sort_data import random_ints
from lib.sort_data import random_ints_negetive
from lib.sort_data import random_floats
from lib.sort_data import random_letters

class Sort_Data:
  pass

sort_data = Sort_Data()
sort_data.random_ints = random_ints
sort_data.random_ints_negetive = random_ints_negetive
sort_data.random_floats = random_floats
sort_data.random_letters = random_letters

# array namespace
from lib.is_sorted import is_sorted

from lib.bubble_sort import bubble_sort
from lib.bubble_sort import bubble_sort_recursive
from lib.insertion_sort import insertion_sort
from lib.insertion_sort import insertion_sort_recursive
from lib.bucket_sort import bucket_sort
from lib.merge_sort import merge_sort
from lib.quick_sort import quick_sort
from lib.heap_sort import heap_sort

class Array_Sort:
  pass

array_sort = Array_Sort()
array_sort.is_sorted = is_sorted
array_sort.bubble_sort = bubble_sort
array_sort.bubble_sort_recursive = bubble_sort_recursive
array_sort.insertion_sort = insertion_sort
array_sort.insertion_sort_recursive = insertion_sort_recursive
array_sort.bucket_sort = bucket_sort
array_sort.merge_sort = merge_sort
array_sort.quick_sort = quick_sort
array_sort.heap_sort = heap_sort

#linked list namespace
from lib.Single_Linked_List import Single_Linked_List

class Linked_List:
  pass

linked_list = Linked_List()
linked_list.single = Single_Linked_List

# tree namespace
from lib.tree_node import Tree_Node

class Graph_Tree:
  pass

graph_tree = Graph_Tree()
graph_tree.tree_node = Tree_Node