# Nama    : Dyas Arum Paramitha
# NIM     : J0403251092
# Kelas   : A2

# ==========================================================
# Latihan 3: Konversi Matrix ke List
# ==========================================================

def matrixToList(matrix):
    V = len(matrix)
    adj = {i: [] for i in range(V)}

    for i in range(V):
        for j in range(V):
            # Jika ada edge, tambahkan ke adjacency list
            if matrix[i][j] == 1:
                adj[i].append(j)

    return adj

if __name__ == "__main__":
    matrix = [
        [0, 1, 1, 0],
        [1, 0, 1, 0],
        [1, 1, 0, 1],
        [0, 0, 1, 0]
    ]

    adj = matrixToList(matrix)

    print("Adjacency List Representation:")
    for node in adj:
        print(f"{node}:", end=" ")
        for neighbor in adj[node]:
            print(neighbor, end=" ")
        print()