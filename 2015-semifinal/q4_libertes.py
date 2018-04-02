# https://prologin.org/train/2015/semifinal/libertes
height, width = map(int, input().split())
piece_i, piece_j = map(int, input().split())
board = [list(map(int, input().split())) for row in range(height)]

coordinates_to_explore = [(piece_i, piece_j)]
coordinates_explored = set()
free_spaces = set()
while coordinates_to_explore:
    i, j = coordinates_to_explore.pop()
    coordinates_explored.add((i, j))
    for i2, j2 in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
        if 0 <= i2 < height and 0 <= j2 < width:
            if board[i2][j2] == board[piece_i][piece_j] and (i2, j2) not in coordinates_explored:
                coordinates_to_explore.append((i2, j2))
            if board[i2][j2] == 2:
                free_spaces.add((i2, j2))
print(len(free_spaces))
