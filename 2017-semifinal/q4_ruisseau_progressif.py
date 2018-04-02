# https://prologin.org/train/2017/semifinal/ruisseau_progressif
n, v_max = map(int, input().split())
vs = [int(v) - v_max for v in input().split()]
min_cost = float('inf')
cost_below = sum([-v for v in vs if v < 0])
cost_above = 0

for v in vs:
    if v >= 0:
        min_cost = min(min_cost, cost_above + cost_below)
        cost_above += v + 1
    else:
        cost_below -= -v
min_cost = min(min_cost, cost_above + cost_below)
print(min_cost)
