# https://prologin.org/train/2008/semifinal/pathfinder
n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
for diagonal in range(2 * n - 1):
    for i in range(diagonal + 1):
        if i < n and 0 <= diagonal - i < n:
            top = matrix[i - 1][diagonal - i] if i >= 1 else 0
            left = matrix[i][diagonal - i - 1] if diagonal - i >= 1 else 0
            matrix[i][diagonal - i] += max(top, left)
print(matrix[-1][-1])
