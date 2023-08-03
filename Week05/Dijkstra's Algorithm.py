def dijkstra(nodes, distances):
    # These are all the nodes which have not been visited yet
    unvisited = {node: None for node in nodes}
    # It will store the shortest distance from one node to another
    visited = {}
    # Here, 'A' is the source node of the shortest distance
    current = 'A'
    # It will store the predecessors of the nodes
    currentDistance = 0
    unvisited[current] = currentDistance
    # Running the loop while all the nodes have been visited
    while True:
        # iterating through all the unvisited node
        for neighbour, distance in distances[current].items():
            # Iterating through the connected nodes of current_node (for 
            # example, a is connected with b, c, d, e and f having values 2, 5, 2, 7 and 50
            # respectively) and the weight of the edges
            if neighbour not in unvisited: continue
            newDistance = currentDistance + distance
            if unvisited[neighbour] is None or unvisited[neighbour] > newDistance:
                unvisited[neighbour] = newDistance
        # Till now the shortest distance between the source node and target node 
        # has been found. Set the current node as the target node
        visited[current] = currentDistance
        del unvisited[current]
        if not unvisited: break
        candidates = [node for node in unvisited.items() if node[1]]
        current, currentDistance = sorted(candidates, key = lambda x: x[1])[0]
    return visited
 
nodes = ('A', 'B', 'C', 'D', 'E', 'F')
distances = {
    'A': {'B': 2, 'C': 5, 'D': 2, 'E': 7, 'F': 50},
    'B': {'C': 2, 'D': 1, 'E': 2, 'F':60},
    'C': {'B': 3, 'E': 2, 'F': 90},
    'D': {'E': 1, 'F': 3},
    'E': {'D': 4, 'F': 4},
    'F': {}}
 
print(dijkstra(nodes, distances))