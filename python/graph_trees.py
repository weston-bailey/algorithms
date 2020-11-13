from lib import graph_tree

# root = graph_tree.tree_node(5)
# root.insert_node(3)
# root.insert_node(7)
# root.insert_node(56)
# root.insert_node(560)
# root.insert_node(-3)
# root.insert_node(.1)

# root.print_values()

# directed graph

# import dictionary for graph
from collections import defaultdict
 
# function for adding edge to graph
graph = defaultdict(list)

def addEdge(graph,u,v):
    graph[u].append(v)
 
# definition of function
def generate_edges(graph):
    edges = []
 
    # for each node in graph
    for node in graph:
         
        # for each neighbour node of a single node
        for neighbour in graph[node]:
             
            # if edge exists then append
            edges.append((node, neighbour))
    return edges

def detect_route(graph, start, end, path: list = []):
    path = path + [start]
    if start == end:
        return path
    for node in graph[start]:
        if node not in path:
            newpath = detect_route(graph, node, end, path)
            if newpath:
                return newpath
  # return False



  



# declaration of graph as dictionary
addEdge(graph,'a','c')
addEdge(graph,'b','c')
addEdge(graph,'b','e')
addEdge(graph,'c','d')
addEdge(graph,'c','e')
addEdge(graph,'c','a')
addEdge(graph,'c','b')
addEdge(graph,'e','b')
addEdge(graph,'d','c')
addEdge(graph,'e','c')
 
# to print generated graph
print(generate_edges(graph)) 

solution = detect_route(graph, 'a', 'c')

# print(graph)

print(solution)


