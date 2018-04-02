# https://prologin.org/train/2018/semifinal/sucre_sale

n, p = map(int, input().split())
m = int(input())
clients = [0, 0, 0]  # sucré, salé, quelconque
for _ in range(m):
    clients[int(input())] += 1
count = 0
n -= clients[0]
p -= clients[1]
if n < 0:
    count += -n
    n = 0
if p < 0:
    count += -p
    p = 0
if clients[2] > n + p:
    count += clients[2] - (n + p)
print(count)
