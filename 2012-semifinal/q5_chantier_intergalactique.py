# https://prologin.org/train/2012/semifinal/chantier_intergalactique
n_v = int(input())
n_e = int(input())
adj = {v: {} for v in range(n_v)}
for _ in range(n_e):
    u, v, weight = map(int, input().split())
    if v in adj[u]:
        adj[u][v] = min(adj[u][v], weight)
        adj[v][u] = adj[u][v]
    else:
        adj[u][v] = weight
        adj[v][u] = weight

added = []
d = {v: float('inf') for v in range(n_v)}
prev = {v: None for v in range(n_v)}
d[0] = 0
prev[0] = 0
adj[0][0] = 0
total_cost = 0
while len(added) != n_v:
    u = min(d.keys(), key=lambda v: d[v] if v not in added else float('inf'))
    d[u] = 0
    total_cost += adj[u][prev[u]]
    added.append(u)
    for v, weight in adj[u].items():
        if v not in added:
            if d[u] + weight < d[v]:
                d[v] = d[u] + weight
                prev[v] = u
print(total_cost)
