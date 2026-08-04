import copy

G = [
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1],
    [0, 0, 0, 0],
]
def warshall(G):
    n = len(G)
    W = copy.deepcopy(G)
    for k in range(0, n):
        for i in range(0, n):
            for j in range(0, n):
                W[i][j] = W[i][j] or (W[i][k] and W[k][j])
    return W
answer = warshall(G)
for row in answer:
    print(row)