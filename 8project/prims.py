# ---------------------------------------------------------
# PRIM'S ALGORITHM USING FUNCTIONS
# Minimum Spanning Tree
# ---------------------------------------------------------


# This function prints a line of '=' characters.
def print_line(length=60):
    print("=" * length)


# ---------------------------------------------------------
# PRIM'S ALGORITHM
# ---------------------------------------------------------

def prim(vertices, graph):

    # visited[i] tells whether vertex i has already
    # been included in the Minimum Spanning Tree.
    #
    # We use vertices 1, 2, ..., V, so we need V + 1
    # positions. Position 0 is unused.
    visited = [False] * (vertices + 1)


    # Store the edges selected for the MST.
    mst = []


    # Store the total weight of the MST.
    total_weight = 0


    # -----------------------------------------------------
    # STARTING VERTEX
    # -----------------------------------------------------

    # Prim's algorithm can start from any vertex.
    # Here, we start from vertex 1.
    start = 1

    # Mark the starting vertex as visited.
    visited[start] = True


    # -----------------------------------------------------
    # DISPLAY HEADER
    # -----------------------------------------------------

    print_line()

    print("                    PRIM'S ALGORITHM")

    print_line()

    print("\n[1] Constructing Minimum Spanning Tree\n")

    print(f"{'Edge':<12}{'Weight':<12}{'Decision':<20}")

    print("-" * 45)


    # -----------------------------------------------------
    # MAIN PRIM'S ALGORITHM
    # -----------------------------------------------------

    # We need exactly V - 1 edges in the MST.
    for _ in range(vertices - 1):

        # Store the minimum edge found in this iteration.
        min_weight = float("inf")

        # Store the vertices of the minimum edge.
        min_u = -1
        min_v = -1


        # -------------------------------------------------
        # FIND THE CHEAPEST EDGE
        # -------------------------------------------------

        # Check every vertex.
        for u in range(1, vertices + 1):

            # We only consider vertices that are already
            # part of the MST.
            if visited[u]:

                # Check all edges connected to u.
                for v, weight in graph[u]:

                    # We are interested in an edge that
                    # connects the MST to an unvisited vertex.
                    if not visited[v] and weight < min_weight:

                        # This is currently the cheapest edge.
                        min_weight = weight

                        min_u = u
                        min_v = v


        # -------------------------------------------------
        # ADD THE SELECTED EDGE
        # -------------------------------------------------

        # If no edge was found, the graph is disconnected.
        if min_u == -1:

            print("\nGraph is disconnected.")
            print("Minimum Spanning Tree cannot be formed.")

            return


        # Mark the new vertex as visited.
        visited[min_v] = True


        # Add the selected edge to the MST.
        mst.append((min_u, min_v, min_weight))


        # Add its weight to the total.
        total_weight += min_weight


        # Display the selected edge.
        print(
            f"{min_u} - {min_v:<8}"
            f"{min_weight:<12}"
            f"{'ACCEPTED':<20}"
        )


    # -----------------------------------------------------
    # DISPLAY FINAL MST
    # -----------------------------------------------------

    print()

    print_line()

    print("                 MINIMUM SPANNING TREE")

    print_line()

    print()

    print(f"{'Edge':<12}{'Weight':<12}")

    print("-" * 24)


    # Display every edge in the MST.
    for edge in mst:

        # Get source vertex.
        u = edge[0]

        # Get destination vertex.
        v = edge[1]

        # Get weight.
        weight = edge[2]

        print(f"{u} - {v:<8}{weight:<12}")


    # -----------------------------------------------------
    # DISPLAY FINAL RESULT
    # -----------------------------------------------------

    print()

    print_line()

    print(f"Total MST Weight : {total_weight}")

    print(f"Edges in MST     : {len(mst)}")

    print_line()


# ---------------------------------------------------------
# MAIN FUNCTION
# ---------------------------------------------------------

def main():

    # Display program heading.
    print_line()

    print("              MINIMUM SPANNING TREE")

    print("                    PRIM'S ALGORITHM")

    print_line()


    # Input number of vertices.
    vertices = int(input("\nEnter number of vertices: "))


    # Input number of edges.
    edges_count = int(input("Enter number of edges: "))


    # -----------------------------------------------------
    # CREATE GRAPH
    # -----------------------------------------------------

    # graph[i] will contain all edges connected to vertex i.
    #
    # Example:
    #
    # graph[1] = [(3, 2), (2, 4)]
    #
    # means:
    # 1 -> 3 has weight 2
    # 1 -> 2 has weight 4
    graph = [[] for _ in range(vertices + 1)]


    print("\nEnter edges in the format:")

    print("Source Destination Weight\n")


    # -----------------------------------------------------
    # INPUT EDGES
    # -----------------------------------------------------

    for i in range(edges_count):

        # Read source, destination and weight.
        u, v, weight = map(
            int,
            input(f"Edge {i + 1}: ").split()
        )


        # Since the graph is undirected,
        # store the edge in both directions.
        graph[u].append((v, weight))
        graph[v].append((u, weight))


    print()


    # Run Prim's algorithm.
    prim(vertices, graph)


# ---------------------------------------------------------
# PROGRAM STARTS HERE
# ---------------------------------------------------------

if __name__ == "__main__":
    main()