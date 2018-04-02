# https://prologin.org/train/2015/semifinal/ecoulement
n = int(input())
cells = [list(map(int, input().split())) for _ in range(n)]

for i in range(1, n):
    row = cells[i]
    for j, cell in enumerate(row):
        above_left = cells[i - 1][j - 1] if j != 0 else float('inf')
        above_right = cells[i - 1][j] if j <= i - 1 else float('inf')
        cells[i][j] += min(above_left, above_right)
print(max(cells[-1]))
