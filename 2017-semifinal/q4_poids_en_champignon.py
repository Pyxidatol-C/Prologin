# https://prologin.org/train/2017/semifinal/poids_en_champignons

n, goal = map(int, input().split())
weights = list(map(int, input().split()))

matrix = [[False] * (goal + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    for s in range(goal + 1):
        if s >= weights[i - 1]:
            matrix[i][s] = matrix[i - 1][s] or weights[i - 1] == s or matrix[i - 1][s - weights[i - 1]]
        else:
            matrix[i][s] = matrix[i - 1][s] or weights[i - 1] == s

print("OUI" if matrix[-1][-1] else "NON")
