# https://prologin.org/train/2015/qualification/expert_itinerant
from heapq import heappush, heappop, heapify

n_v, n_e, n_r = map(int, input().split())
adj = {v: {} for v in range(n_v)}
sources = []
to_find = []
for _ in range(n_e):
    u, v, w = map(int, input().split())
    adj[u - 1][v - 1] = w
for _ in range(n_r):
    src, dest = map(int, input().split())
    if src - 1 not in sources:
        sources.append(src - 1)
    to_find.append((src - 1, dest - 1))


def dijkstra(s):
    d = {v: float('inf') for v in range(n_v)}
    d[s] = 0
    explored = set()
    q = [(dist, node) for node, dist in d.items()]
    heapify(q)
    while len(explored) != n_v:
        n1 = heappop(q)[1]
        explored.add(n1)
        for n2, weight in adj[n1].items():
            if n2 not in explored:
                alt = d[n1] + weight
                if alt < d[n2]:
                    d[n2] = alt
                    heappush(q, (alt, n2))
    return d
# # Custom implementation of binary heap is too slow
# class MinHeap:
#     def __init__(self):
#         self.heap = []
#
#     def add(self, i):
#         self.heap.append(i)
#         self.heapify()
#
#     def heapify(self):
#         def _heapify(i):
#             if len(self.heap) < 2 * i + 2:
#                 return
#             if len(self.heap) > 2 * i + 2:
#                 i2 = min([
#                     (self.heap[2 * i + 1], 2 * i + 1),
#                     (self.heap[2 * i + 2], 2 * i + 2)
#                 ])[1]
#             else:
#                 i2 = 2 * i + 1
#             if self.heap[i] > self.heap[i2]:
#                 self.heap[i], self.heap[i2] = self.heap[i2], self.heap[i]
#                 _heapify(i2)
#
#         for j in range(len(self.heap)):
#             _heapify(len(self.heap) - j - 1)
#
#     def extract(self):
#         min_ = self.heap[0]
#         self.heap = self.heap[1:]
#         self.heapify()
#         return min_
#
#
# def dijkstra(s):
#     d = {v: float('inf') for v in range(n_v)}
#     d[s] = 0
#     explored = set()
#     heap = MinHeap()
#     for node, dist in d.items():
#         heap.add((dist, node))
#     while len(explored) != n_v:
#         n1 = heap.extract()[1]
#         explored.add(n1)
#         for n2, weight in adj[n1].items():
#             if n2 not in explored:
#                 alt = d[n1] + weight
#                 if alt < d[n2]:
#                     d[n2] = alt
#                     heap.add((alt, n2))
#     return d


distances = {src: dijkstra(src) for src in sources}
for u, v in to_find:
    print(distances[u][v])
