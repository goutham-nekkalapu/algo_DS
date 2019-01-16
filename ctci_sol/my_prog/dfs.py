
# depth first search algoritm on graph 

def form_graph():
    graph = {}
    graph['a'] = ['b', 'c', 'd']
    graph['b'] = ['a']
    graph['c'] = ['a', 'f']
    graph['d'] = ['a', 'f', 'e']
    graph['f'] = ['c', 'd', 'g']
    graph['e'] = ['d']
    graph['g'] = ['f']
    print ("the graph is : ",graph)
    return graph 

def dfs(graph):
    nodes = graph.keys()
    print ("nodes of graph are : ",nodes)
    track_visited = {}   

    for node in nodes:
        track_visited[node] = False
    print (" the track dict is :", track_visited)

    # logic for DFS 
    dfs = [] 
    if not is_visited(nodes[0], track_visited):
       dfs.append(nodes[0])

    for node in graph[nodes[0]]:
        if not is_visited(node,track_visited):
            dfs.append(node)

def search(node, graph, track_visited, dfs_list):
   
    if len(graph[node]) == 0:
       return dfs_list, track_visited
    
    dfs_list = visit(node,dfs_list)
    track_visited[node] = True

    for i in graph[node]:
        if not is_visited
           dfs_list, track_visited = search(node, graph, track_visited, dfs_list)


if __name__ == "__main__":
    print ("hello")
    graph = form_graph()
    dfs(graph)


