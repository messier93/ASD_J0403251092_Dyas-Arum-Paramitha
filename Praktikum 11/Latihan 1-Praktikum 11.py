# Nama    : Dyas Arum Paramitha
# NIM     : J0403251092
# Kelas   : A2

# ==========================================================
# Latihan 1: Membuat Adjacency Matrix
# ==========================================================

def createGraph(V, edges):
    mat = [[0 for _ in range(V)] for _ in range(V)]
    for it in edges:
        u = it[0]
        v = it[1]
        mat[u][v] = 1
        mat[v][u] = 1  # undirected
    return mat

if __name__ == "__main__":
    V = 4  
    edges = [[0, 1], [0, 2], [1, 2], [2, 3]]  

    mat = createGraph(V, edges)

    print("Adjacency Matrix Representation:")
    for i in range(V):
        for j in range(V):
            print(mat[i][j], end=" ")
        print()