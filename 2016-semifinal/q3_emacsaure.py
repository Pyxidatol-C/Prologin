# https://prologin.org/train/2016/semifinal/emacsaure
# TODO does not pass performance tests

m, n = map(int, input().split())
terrain = [
    list(input()) for _ in range(m)
]
r, c = 0, 0
lava_pos = -1
while c != n - 1:
    if terrain[r][c + 1] == '.':
        c += 1
    elif r < m - 1 and terrain[r + 1][c] == '.':
        r += 1
    else:
        print(0)
        break
    lava_pos += 0.5
    if lava_pos >= c:
        print(0)
        break
else:
    print(1)
