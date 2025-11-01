graph = {'A': ['B', 'C'],
         'B': ['D','E'],
         'C': ['F','G'],
         'D': [],
         'E': [],
         'F': [],
         'G': []}

start_node = 'A'
goal_node = 'G'

def depth_limited_search(node, goal, limit, path, graph):
    """Searches for goal up to a depth limit. Returns path if found, None otherwise."""
    
    if node == goal:
        return path
    
    if limit <= 0:
        return None
    
    for neighbour in graph.get(node, []):
        if neighbour not in path:
            result = depth_limited_search(neighbour, goal, limit-1, path + [neighbour], graph)
            if result is not None:
                return result
    
    return None 

def iterative_deepening_search(start,goal,graph,depth_max = 50):
    """Performs iterative deepening search to find a path from start to goal."""

    for depth in range(depth_max):
        print(f"Depth: {depth}")
        result = depth_limited_search(start, goal, depth, [start], graph)
        if result is not None:
            print(f"Goal is at depth: {depth}")
            return result

    print("Goal node not found :(")
    return None