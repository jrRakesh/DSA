
def print_line(length=60):
    print("=" * length)

def prim(vertices, graph):

    visited = [False] * (vertices + 1)

    mst = []
    total_weight = 0
    start = 1
    visited[start] = True

    print_line()

    print("                    PRIM'S ALGORITHM")

    print_line()

    print("\n[1] Constructing Minimum Spanning Tree\n")

    print(f"{'Edge':<12}{'Weight':<12}{'Decision':<20}")

    print("-" * 45)

    for _ in range(vertices - 1):
        # Minimum weight at beginning be infinity
        min_weight = float("inf")
        min_u = -1
        min_v = -1

        for u in range(1, vertices + 1):

            if visited[u]:
                for v, weight in graph[u]:

                    if not visited[v] and weight < min_weight:
                        min_weight = weight
                        min_u = u
                        min_v = v

        # If no edge was found, the graph is disconnected.
        if min_u == -1:

            print("\nGraph is disconnected.")
            print("Minimum Spanning Tree cannot be formed.")

            return

        visited[min_v] = True

        mst.append((min_u, min_v, min_weight))

        total_weight += min_weight

        print(
            f"{min_u} - {min_v:<8}"
            f"{min_weight:<12}"
            f"{'ACCEPTED':<20}"
        )

    print()

    print_line()

    print("                 MINIMUM SPANNING TREE")

    print_line()

    print()

    print(f"{'Edge':<12}{'Weight':<12}")

    print("-" * 24)

    for edge in mst:
        u = edge[0]
        v = edge[1]
        weight = edge[2]
        print(f"{u} - {v:<8}{weight:<12}")

    print()

    print_line()

    print(f"Total MST Weight : {total_weight}")

    print(f"Edges in MST     : {len(mst)}")

    print_line()


print_line()

print("               MINIMUM SPANNING TREE")

print_line()

vertices = int(input("\nEnter number of vertices: "))
edges_count = int(input("Enter number of edges: "))
graph = [[] for _ in range(vertices + 1)]

print("\nEnter edges in the format:")

print("Source Destination Weight\n")

for i in range(edges_count):
    u, v, weight = map(int, input(f"Edge {i + 1}: ").split())
    graph[u].append((v, weight))
    graph[v].append((u, weight))

print()

prim(vertices, graph)
