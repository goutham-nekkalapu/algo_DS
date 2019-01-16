
"""
problem 4.1 
given a directed graph find if there is a route b/w two nodes 

"""

# search if there is a path b/w point 'A' and 'B' in a directed graph  
def bfs_search(graph, start, end):
    visited = []
    queue= [start]

    while queue:
        vertex = queue.pop(0)
        if vertex[0] not in visited and vertex[1] == 1:
            if vertex[0] == end[0]:
               return True
            visited.append(vertex[0])
            for node in graph[vertex[0]]:
                if node[0] not in visited:
                    queue.append(node)
    #return visited
    return False

if __name__ == "__main__":

   # directed graph 
   graph =  {
                'A': [('B',1), ('C',1)],
                'B': [('A',0), ('D',1), ('E',0)],
                'C': [('A',0), ('F',1)],
                'D': [('B',0)],
                'E': [('B',1), ('F',0)],
                'F': [('C',0), ('E',1)]
            }

   # expected : True
   is_path = bfs_search(graph,('C',1), ('D',1))
   print(is_path)

   # expected : False
   is_path = bfs_search(graph,('C',1), ('A',1))
   print(is_path)
