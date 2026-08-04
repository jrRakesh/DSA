G = {
    'A': {'B', 'Q'},
    'B': {'A', 'T'},
    'Q': {'A','T','Y'},
    'T': {'B', 'Q', 'Y','Z'},
    'Y': {'Q', 'T', 'S'},
    'S': {'Y', 'Z', 'W'},
    'Z': {'T', 'S', 'W'},
    'W': {'Z', 'S'},
}

def BFS(graph, start_vertex):
    visited = []
    stack = []

    stack.append(start_vertex)

    while len(stack) >0:
        current_vertex = stack.pop(0)

        visited.append(current_vertex)

        for neighbor in graph[current_vertex]:
            if neighbor not in stack and neighbor not in visited:
                stack.append(neighbor)

    return visited

print("DFS Traversal sequence is : ",BFS(G,'A'))