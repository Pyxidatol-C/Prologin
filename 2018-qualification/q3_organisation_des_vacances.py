# https://prologin.org/train/2018/qualification/organisation_des_vacances
n = int(input())
dates = []
for _ in range(n):
    start, end, cost = map(int, input().split())
    dates.append((start, cost))
    dates.append((end, -cost))
dates.sort(key=lambda d: d[0])

min_cost1 = float('inf')
min_cost = float('inf')

for date, cost in dates:
    if cost < 0:
        min_cost1 = min(min_cost1, -cost)
    else:
        min_cost = min(min_cost, cost + min_cost1)

if min_cost == float('inf'):
    print(-1)
else:
    print(min_cost)
