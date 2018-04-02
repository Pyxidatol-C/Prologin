# https://prologin.org/train/2018/semifinal/plus_de_crepes
from heapq import heapify, heappush, heappop

n_v, n_e = map(int, input().split())
g = {node: {} for node in range(n_v)}
for _ in range(n_e):
    u_, v_, w_ = map(int, input().split())
    g[u_ - 1][v_ - 1] = w_
    g[v_ - 1][u_ - 1] = w_


def bfs(src):
    to_explore = {src}
    explored = set()
    while to_explore:
        to_explore_ = set()
        for u in to_explore:
            explored.add(u)
            if u in vertices:
                vertices.remove(u)
            for v in g[u]:
                if v not in explored:
                    to_explore_.add(v)
        to_explore = to_explore_
    return explored


def dijkstra(src, vs):
    d = {node: float('inf') if node != src else 0 for node in vs}
    q = [(dist, node) for node, dist in d.items()]
    heapify(q)
    explored = set()
    while len(explored) != len(vs):
        u = heappop(q)[1]
        explored.add(u)
        for v, w in g[u].items():
            if v not in explored:
                if d[v] > d[u] + w:
                    d[v] = d[u] + w
                    heappush(q, (d[v], v))
    return d


total = 0
vertices = set(range(n_v))
while vertices:
    nodes = bfs(next(iter(vertices)))
    for node in nodes:
        total += sum(dijkstra(node, nodes).values())
print(total)
