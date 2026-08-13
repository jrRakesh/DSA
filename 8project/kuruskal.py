# ---------------------------------------------------------
# KRUSKAL'S ALGORITHM USING FUNCTIONS
# Minimum Spanning Tree
# ---------------------------------------------------------


# This function prints a line of '=' characters.
# It is only used to make the output look cleaner.
def print_line(length=60):
    print("=" * length)


# ---------------------------------------------------------
# FIND FUNCTION
# ---------------------------------------------------------

# parent is the array that stores the parent of every vertex.
# x is the vertex whose root we want to find.
def find(parent, x):

    # If x is its own parent, then x is the root.
    if parent[x] == x:
        return x

    # Otherwise, recursively find the root of x.
    #
    # Path compression:
    # After finding the root, directly make x point to it.
    parent[x] = find(parent, parent[x])

    # Return the root.
    return parent[x]


# ---------------------------------------------------------
# UNION FUNCTION
# ---------------------------------------------------------

# This function joins the sets containing u and v.
#
# parent -> stores the parent of each vertex
# rank   -> helps keep the tree balanced
# u, v   -> two vertices of the edge
def union(parent, rank, u, v):

    # Find the root of vertex u.
    root_u = find(parent, u)

    # Find the root of vertex v.
    root_v = find(parent, v)

    # If both vertices have the same root,
    # they already belong to the same set.
    #
    # Adding this edge would create a cycle.
    if root_u == root_v:
        return False

    # If the rank of root_u is smaller,
    # make root_v the new root.
    if rank[root_u] < rank[root_v]:
        root_u, root_v = root_v, root_u

    # Make root_u the parent of root_v.
    parent[root_v] = root_u

    # If both trees had the same rank,
    # the rank of the new root increases by 1.
    if rank[root_u] == rank[root_v]:
        rank[root_u] += 1

    # The edge was successfully added.
    return True


# ---------------------------------------------------------
# KRUSKAL'S ALGORITHM
# ---------------------------------------------------------

def kruskal(vertices, edges):

    # Sort all edges according to their weight.
    #
    # Each edge is stored as:
    # (source, destination, weight)
    #
    # edge[2] means the weight.
    edges.sort(key=lambda edge: edge[2])


    # -----------------------------------------------------
    # CREATE DISJOINT SET
    # -----------------------------------------------------

    # We are using vertices 1, 2, 3, ..., V.
    #
    # Therefore we need V + 1 positions.
    #
    # Position 0 will simply remain unused.
    parent = list(range(vertices + 1))

    # Initially, rank of every vertex is 0.
    rank = [0] * (vertices + 1)


    # This list will store the edges selected for the MST.
    mst = []

    # This variable stores the total weight of the MST.
    total_weight = 0


    # -----------------------------------------------------
    # DISPLAY SORTED EDGES
    # -----------------------------------------------------

    print_line()

    print("                 KRUSKAL'S ALGORITHM")

    print_line()

    print("\n[1] Sorted Edges\n")

    print(f"{'Edge':<10}{'Weight':<10}")

    print("-" * 20)


    # Go through every edge after sorting.
    for edge in edges:

        # Extract the source vertex.
        u = edge[0]

        # Extract the destination vertex.
        v = edge[1]

        # Extract the weight.
        weight = edge[2]

        # Display the edge.
        print(f"{u:<5}-{v:<4}{weight:<10}")


    # -----------------------------------------------------
    # CONSTRUCT MST
    # -----------------------------------------------------

    print("\n[2] Constructing Minimum Spanning Tree\n")

    print(f"{'Edge':<12}{'Weight':<12}{'Decision':<20}")

    print("-" * 45)


    # Process each edge in increasing order of weight.
    for edge in edges:

        # Get the vertices and weight.
        u = edge[0]
        v = edge[1]
        weight = edge[2]


        # Try to join u and v.
        #
        # union() returns:
        # True  -> edge can be added
        # False -> edge creates a cycle
        added = union(parent, rank, u, v)


        # If the edge was successfully added...
        if added:

            # Add the edge to our MST.
            mst.append(edge)

            # Add its weight to the total MST weight.
            total_weight += weight

            # Display that the edge was accepted.
            print(
                f"{u} - {v:<8}"
                f"{weight:<12}"
                f"{'ACCEPTED':<20}"
            )


        # Otherwise, the edge creates a cycle.
        else:

            # Display that the edge was rejected.
            print(
                f"{u} - {v:<8}"
                f"{weight:<12}"
                f"{'REJECTED (Cycle)':<20}"
            )


        # A spanning tree containing V vertices
        # always contains exactly V - 1 edges.
        #
        # Therefore, once we have V - 1 edges,
        # we can stop.
        if len(mst) == vertices - 1:
            break


    # -----------------------------------------------------
    # DISPLAY MST
    # -----------------------------------------------------

    print()

    print_line()

    print("                 MINIMUM SPANNING TREE")

    print_line()

    print()

    print(f"{'Edge':<12}{'Weight':<12}")

    print("-" * 24)


    # Display every edge selected in the MST.
    for edge in mst:

        # Get source vertex.
        u = edge[0]

        # Get destination vertex.
        v = edge[1]

        # Get edge weight.
        weight = edge[2]

        # Display the edge.
        print(f"{u} - {v:<8}{weight:<12}")


    # -----------------------------------------------------
    # DISPLAY FINAL RESULT
    # -----------------------------------------------------

    print()

    print_line()

    # Display total MST weight.
    print(f"Total MST Weight : {total_weight}")

    # Display number of edges in MST.
    print(f"Edges in MST     : {len(mst)}")

    print_line()


# ---------------------------------------------------------
# MAIN FUNCTION
# ---------------------------------------------------------

def main():

    # Display program heading.
    print_line()

    print("              MINIMUM SPANNING TREE")

    print("                 KRUSKAL'S ALGORITHM")

    print_line()


    # Ask the user for the number of vertices.
    vertices = int(input("\nEnter number of vertices: "))


    # Ask the user for the number of edges.
    edges_count = int(input("Enter number of edges: "))


    # Create an empty list to store all edges.
    edges = []


    # Tell the user how to enter an edge.
    print("\nEnter edges in the format:")

    print("Source Destination Weight\n")


    # Repeat according to the number of edges.
    for i in range(edges_count):

        # Take three integers from the user.
        #
        # Example:
        # 1 3 2
        #
        # u = 1
        # v = 3
        # weight = 2
        u, v, weight = map(
            int,
            input(f"Edge {i + 1}: ").split()
        )


        # Store the edge as a tuple.
        #
        # Example:
        # (1, 3, 2)
        edges.append((u, v, weight))


    # Print an empty line.
    print()


    # Call Kruskal's algorithm.
    kruskal(vertices, edges)


# ---------------------------------------------------------
# PROGRAM STARTS HERE
# ---------------------------------------------------------

# This condition makes sure main() runs only when
# this file is executed directly.
if __name__ == "__main__":
    main()