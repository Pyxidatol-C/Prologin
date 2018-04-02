# https://prologin.org/train/2018/semifinal/plus_de_crepes
# TODO debug

v, e = map(int, input().split())
adj = {x: set() for x in range(1, v + 1)}
for i in range(e):
    x, y, w = map(int, input().split())
    adjx = (y, w)
    adjy = (x, w)
    adj[x].add(adjx)
    adj[y].add(adjy)


def exist_in_list_of_lists(x, ls):
    for i in ls:
        if x in i:
            return True
    else:
        return False


def bfs(s, adj):
    level = -1
    visited = set()
    to_visit = {s}
    while to_visit:
        next_ = set()
        for node in to_visit:
            visited.add(node)
            for i in adj[node]:
                if i[0] not in visited:
                    next_.add(i[0])
        level += 1
        to_visit = next_
    return visited


def dijkstra(s, adj, connected, idx):
    d = {i: float("inf") for i in connected[idx]}  # something wrong with length
    d[s] = 0
    visited = set()  # keep them the ints, the nodes, not plus the weight tuple
    while len(visited) != len(adj):  # maybe include the use of "length" argument? !!!
        i = min([node for node in d.keys() if node not in visited], key=lambda node: d[node])
        for j, weight, in adj[i]:
            if j not in visited:
                if d[j] > d[i] + weight:
                    d[j] = d[i] + weight
        visited.add(i)
    return sum(d.values())
