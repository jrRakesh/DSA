def kruskal(vertices, edges):

    def get_weight(edge):
        return edge[2]

    edges.sort(key=get_weight)

    # Initially, every vertex is its own parent
    parent = list(range(vertices + 1))

    mst = []

    total = 0

    for u, v, weight in edges:

        root_u = find(parent, u)
        root_v = find(parent, v)

        if root_u != root_v:

            parent[root_v] = root_u
            mst.append((u, v, weight))
            total += weight

        if len(mst) == vertices - 1:
            break

    print("\nMinimum Spanning Tree:")

    for u, v, weight in mst:
        print(u, "-", v, "weight =", weight)

    print("Total weight =", total)


def find(parent, x):

    if parent[x] == x:
        return x

    return find(parent, parent[x])

vertices = int(input("Enter number of vertices: "))
edges_count = int(input("Enter number of edges: "))

edges = []

print("\nEnter edges in the format:")
print("Source Destination Weight\n")

for i in range(edges_count):

    u, v, weight = map(int, input(f"Edge {i+1} : ").split())

    edges.append((u, v, weight))

kruskal(vertices, edges)