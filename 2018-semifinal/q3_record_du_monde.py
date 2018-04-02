# https://prologin.org/train/2018/semifinal/record_du_monde

height, width = map(int, input().split())
heat_map = [[0] * width for _ in range(height)]
for _ in range(int(input())):
    i, j, heat = map(int, input().split())
    heat_map[i][j] += heat
    for radius in range(1, heat):
        to_update = set()
        for j2 in range(j - radius, j + radius + 1):
            to_update.add((i - radius, j2))
            to_update.add((i + radius, j2))
        for i2 in range(i - radius, i + radius + 1):
            to_update.add((i2, j - radius))
            to_update.add((i2, j + radius))
        for i3, j3 in to_update:
            if 0 <= i3 < height and 0 <= j3 < width:
                heat_map[i3][j3] += heat - radius
print(max([max(row) for row in heat_map]))
