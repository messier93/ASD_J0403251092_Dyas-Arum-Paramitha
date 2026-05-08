# Nama    : Dyas Arum Paramitha
# NIM     : J0403251092
# Kelas   : A2

# ==========================================================
# Latihan 2: Membuat Adjacency List
# ==========================================================

def createGraph(V, edges):
    adj = {node: [] for node in V}

    for it in edges:
        u = it[0]
        v = it[1]
        adj[u].append(v)
        adj[v].append(u)

    return adj

if __name__ == "__main__":
    V = ['A', 'B', 'C', 'D']
    edges = [['A', 'B'], ['A', 'C'], ['B', 'D'], ['C', 'D']]

    adj = createGraph(V, edges)

    print("Adjacency List Representation:")
    for node in V:
        print(f"{node}:", end=" ")
        for neighbor in adj[node]:
            print(neighbor, end=" ")
        print()