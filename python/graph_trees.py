from lib import graph_tree

root = graph_tree.tree_node(5)
root.insert_node_sorted(3)
root.insert_node_sorted(7)
root.insert_node_sorted(56)
root.insert_node_sorted(560)
root.insert_node_sorted(-3)
root.insert_node_sorted(.1)

root.print_values()