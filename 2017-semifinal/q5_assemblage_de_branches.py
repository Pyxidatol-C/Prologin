# https://prologin.org/train/2017/semifinal/assemblage_de_branches

n_v, n_e = map(int, input().split())
adj = {v: set() for v in range(n_v)}
for _ in range(n_e):
    u, v = map(int, input().split())
    adj[u].add(v)
    adj[v].add(u)

vs = set(range(n_v))
total = 0


while vs:
    to_visit = {next(iter(vs))}
    visited = set()
    for i in range(2):
        depth = -1
        (farthest_node,) = to_visit
        while to_visit:
            to_visit_ = set()
            for u in to_visit:
                visited.add(u)
                farthest_node = u
                to_visit_ |= {v for v in adj[u] if v not in visited}
            to_visit = to_visit_
            depth += 1
        if i == 0:
            to_visit = {farthest_node}
            visited = set()
        else:

            total += depth
            vs -= visited
print(total)
