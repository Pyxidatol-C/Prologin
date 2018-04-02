# https://prologin.org/train/2018/qualification/faites_place

n = int(input())
num_m = int(input())
pos = list(map(int, input().split()))

max_influence = max(
    [pos[0] - .5]
    + [(pos[i] - pos[i - 1]) / 2 for i in range(1, num_m)]
    + [n - pos[-1] - .5]
)
print(int(max_influence))
