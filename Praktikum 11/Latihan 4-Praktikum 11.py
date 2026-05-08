# Nama    : Dyas Arum Paramitha
# NIM     : J0403251092
# Kelas   : A2
# ==========================================================
# Latihan 4: Studi Kasus Dunia Nyata
# ==========================================================

# Adjacency list menggunakan dictionary
graph = {
    "Sparxie":            ["Silver Wolf LV.999", "Yao Guang", "Evanescia"],
    "Silver Wolf LV.999": ["Sparxie", "Yao Guang", "Nihilux"],
    "Yao Guang":          ["Sparxie", "Silver Wolf LV.999", "Evanescia"],
    "Evanescia":          ["Sparxie", "Yao Guang", "Nihilux"],
    "Nihilux":            ["Silver Wolf LV.999", "Evanescia"]
}

# Adjacency matrix dari graph
nodes = ["Sparxie", "Silver Wolf LV.999", "Yao Guang", "Evanescia", "Nihilux"]
index = {node: i for i, node in enumerate(nodes)}
V     = len(nodes)
matrix = [[0] * V for _ in range(V)]

for u in graph:
    for v in graph[u]:
        matrix[index[u]][index[v]] = 1

# ==========================================================
# Output
# ==========================================================

COL = 22

print("=" * (COL + V * 4))
print("Planarcadia Network")
print("=" * (COL + V * 4))

print("\n[Node yang terdaftar]")
for i, node in enumerate(nodes):
    print(f"  {i} - {node}")

print("\n[Hubungan antar node / Edge]")
printed = set()
for u in graph:
    for v in graph[u]:
        edge = tuple(sorted([u, v]))
        if edge not in printed:
            print(f"  {u} --- {v}")
            printed.add(edge)

print("\n[Adjacency List]")
for node in graph:
    neighbors = ", ".join(graph[node])
    print(f"  {node}: {neighbors}")

print("\n[Adjacency Matrix]")
short = ["Sprx", "SW999", "Yao", "Nescia", "Nhlx"]
print(f"  {'':>{COL}}", " ".join(f"{s:>4}" for s in short))
print(f"  {'-' * (COL + V * 5)}")
for i, row in enumerate(matrix):
    label = nodes[i][:COL]
    print(f"  {label:>{COL}} |", " ".join(f"{val:>4}" for val in row))

print("=" * (COL + V * 4))