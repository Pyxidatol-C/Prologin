# https://prologin.org/train/2017/semifinal/assemblage_de_branches
def bfs(src):
    to_explore = [src]
    level = -1
    explored = []
    while to_explore:
        level += 1
        to_explore_new = []
        for n1 in to_explore:
            explored.append(n1)
            if n1 in remaining:
                remaining.remove(n1)
            for n2 in adj[n1]:
                if n2 not in explored:
                    to_explore_new.append(n2)
        to_explore = to_explore_new
    return level, explored[-1]


n_v, n_e = map(int, input().split())
adj = {node: set() for node in range(n_v)}
for _ in range(n_e):
    u, v = map(int, input().split())
    adj[u].add(v)
    adj[v].add(u)
remaining = set(range(n_v))

sum_lengths = 0
while remaining:
    sum_lengths += bfs(bfs(next(iter(remaining)))[1])[0]
print(sum_lengths)
