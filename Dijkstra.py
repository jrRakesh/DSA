import math
#Dictionary of dictionary
G = {
    'A':{'M':2, 'S':1},
    'M':{'A':2, 'S':3, 'U':1, 'Z':1},
    'S':{'A':1, 'M':3, 'W':4},
    'Z':{'M':1, 'U':3, 'W':4},
    'U':{'S':7, 'M':1, 'Z':3, 'W':1},
    'W':{'Z':4, 'U':1}
}
def initailize(G, start):
    cost = dict()
    previous = dict()
    for vertex in G.keys():
        cost[vertex] = math.inf
        previous[vertex] = None
    cost[start] = 0
    return cost, previous

def relax(u, v, G, cost, previous):
    if cost[v] > cost[u]+G[u][v]:
        cost[v]= cost[u]+G[u][v]
        previous[v]= u
    return cost, previous

def dijkstra(G, start):
    cost, previous = initailize(G, start)
    visited = set()
    PQ ={}
    for vertex in G.keys():
        PQ[vertex] = cost[vertex]
    while(PQ):
        current = min(PQ, key=PQ.get)
        del PQ[current]
        visited.add(current)
        for neighbor in G[current].keys():
            if neighbor not in visited:
                old_cost = cost[neighbor]
                cost, previous = relax(current, neighbor, G, cost, previous)
                if old_cost > cost[neighbor]:
                    PQ[neighbor] = cost[neighbor]
    return cost, previous

def construct_path(previous, vertex):
    path = [vertex]
    while(previous[vertex] != None):
        path.append(previous[vertex])
        vertex = previous[vertex]
    return '->'.join(path[::-1])

start = "A"
cost, previous = dijkstra(G, start)
for vertex in G.keys():
    print(f"Shortest Path from {start} to {vertex} is {construct_path(previous, vertex)} | Cost = {cost[vertex]}")
