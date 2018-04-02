# https://prologin.org/train/2017/qualification/maximise_ton_fun
def main():
    n_v, n_e = map(int, input().split())
    adj = {node: {} for node in range(n_v)}
    for _ in range(n_e):
        x, y, weight = map(int, input().split())
        adj[x][y] = -weight
    # Bellman-Ford
    dist = {node: float('inf') for node in range(n_v)}
    dist[0] = 0
    for _ in range(n_v - 1):
        for u in range(n_v):
            for v, weight in adj[u].items():
                dist[v] = min(dist[v], dist[u] + weight)

    for u in range(n_v):
        for v, weight in adj[u].items():
            if dist[u] + weight < dist[v]:
                print("OVERDOSE DE FUN")
                return
    print(-min(dist.values()))


main()
