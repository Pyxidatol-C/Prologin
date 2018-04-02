# https://prologin.org/train/2014/semifinal/isaac
# https://prologin.org/train/2014/semifinal/newton

n = int(input())
map_ = [list(input()) for _ in range(n)]

candidate_cnt = 0
for i in range(n):
    for j in range(n):
        if map_[i][j] == 'o':
            adj_cnt = 0
            for i2, j2 in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                if 0 <= i2 < n and 0 <= j2 < n:
                    if map_[i2][j2] == 'x':
                        adj_cnt += 1
            if adj_cnt >= 3:
                candidate_cnt += 1
print(candidate_cnt)
