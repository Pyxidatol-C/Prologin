# https://prologin.org/train/2018/qualification/restauration_rapide

m = int(input())
adj = {v: {} for v in range(m + 1)}
for _ in range(m):
    u, v, w = map(int, input().split())
    adj[u][v] = w
    adj[v][u] = w
leaves = [v for v, adj_v in adj.items() if len(adj_v) == 1]
node_count = {v: 1 for v in range(m + 1)}
total = 0
while leaves:
    leaf = leaves.pop()
    (attached_node,) = adj[leaf]
    total += adj[leaf][attached_node] * node_count[leaf] * (m + 1 - node_count[leaf])
    node_count[attached_node] += node_count[leaf]
    del adj[leaf]
    del adj[attached_node][leaf]
    if not adj[attached_node]:
        break
    if len(adj[attached_node]) == 1:
        leaves.append(attached_node)
num_edges = m * (m + 1) / 2
print(int(total / num_edges))
