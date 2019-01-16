
"""
Implementation of dfs and bfs algorithms on a graph

"""
"""
Time complexities of BFS/DFS, when the graph is stored in adjacency list  
O(V + E) ; 
    where V = no of vertices in graph
          E = no of edges in graph

Explanation: In any of the algorithms we do the do the following : 
v1 + (incident edges) + v2 + (incident edges) + .... + vn + (incident edges)
(v1 + v2 + ... + vn) + [(incident_edges v1) + (incident_edges v2) + ... + (incident_edges vn)]
"""

# dfs using recursion
def dfs_recursion(graph, node, visited = None):
    if visited is None:
        visited = []
        
    if node not in visited:
        visited.append(node)
        for n in graph[node]:
            dfs_recursion(graph,n,visited)
        return visited

# dfs using iterative loop
def dfs(graph, start_node):
    stack = [start_node]
    visited = []
    
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.append(vertex)
            for n in graph[vertex]:
                if n not in visited:
                    stack.append(n)
    return visited

# dfs paths using recursion
def dfs_paths_recursion(graph, start, goal, path = None):
    if path is None:
        path = [start]
        
    if start == goal:
        yield path
        
    for next in graph[start]:
        if next not in path:
            yield from dfs_paths_recursion(graph, next, goal, path + [next])
            

# bfs using iteration on an undirected graph 
def bfs(graph, start):
    visited = []
    queue= [start]
    
    while queue:
        vertex = queue.pop(0)              
        if vertex not in visited:
            visited.append(vertex)            
            for node in graph[vertex]:
                if node not in visited:
                    queue.append(node)
    return visited

# bfs using iteration on a directed graph
def bfs_directed(graph, start):
    visited = []
    queue= [start]

    while queue:
        vertex = queue.pop(0)
        if vertex[0] not in visited and vertex[1] == 1:
            visited.append(vertex[0])
            for node in graph[vertex[0]]:
                if node[0] not in visited:
                    queue.append(node)
    return visited


if __name__ == "__main__":
   
   # undirected graph  
   graph =  {
		'A': ['B', 'C'],
                'B': ['A', 'D', 'E'],
       	  	'C': ['A', 'F'],
	        'D': ['B'],
       	        'E': ['B', 'F'],
	        'F': ['C', 'E']
	    }	
    
   # directed graph 
   graph_directed =  {
                'A': [('B',1), ('C',1)],
                'B': [('A',0), ('D',1), ('E',0)],
                'C': [('A',0), ('F',1)],
                'D': [('B',0)],
                'E': [('B',1), ('F',0)],
                'F': [('C',0), ('E',1)]
            }
 
   dfs_out = dfs_recursion(graph,'A')
   print(dfs_out) 

   dfs_out = dfs(graph,'A')
   print(dfs_out)

   # testing
   dfs_paths = list(dfs_paths_recursion(graph, 'A', 'F')) # [['A', 'C', 'F'], ['A', 'B', 'E', 'F']]
   print(dfs_paths)

   bfs_out = bfs(graph,'A')
   print(bfs_out)

   # expected output : ['C', 'F', 'E', 'B', 'D']
   bfs_out = bfs_directed(graph_directed,('C',1)) # find BFS on given graph starting from 'C'
   print(bfs_out)

