# https://prologin.org/train/2016/semifinal/tete_baissee

n = int(input())
rows = [[] for _ in range(n)]
cols = [[] for _ in range(n)]
destination = (-1, -1)
position = (-1, -1)
for r_ in range(n):
    row_ = input()
    for c_, cell_ in enumerate(row_):
        if cell_ == 'T':
            position = (r_, c_)
        if cell_ == 'M':
            destination = (r_, c_)
        if cell_ == 'X':
            rows[r_].append(c_)
            cols[c_].append(r_)


def horizontal(i, j):
    row = [-1] + rows[i] + [n]
    lo, hi = 0, len(row)
    while lo != hi - 1:
        mid = (lo + hi) // 2
        if j < row[mid]:
            hi = mid
        else:
            lo = mid
    return [row[lo] + 1, row[hi] - 1]


def vertical(i, j):
    col = [-1] + cols[j] + [n]
    lo, hi = [0, len(col)]
    while lo != hi - 1:
        mid = (lo + hi) // 2
        if i < col[mid]:
            hi = mid
        else:
            lo = mid
    return [col[lo] + 1, col[hi] - 1]


def main():
    explored = []
    to_explore = [position]
    cnt = 0
    while to_explore:
        new_to_explore = []
        for i, j in to_explore:
            explored.append((i, j))
            for j2 in horizontal(i, j):
                if i == destination[0]:
                    if min(j, j2) <= destination[1] <= max(j, j2):
                        print(cnt)
                        return
                if (i, j2) not in explored:
                    new_to_explore.append((i, j2))
            for i2 in vertical(i, j):
                if j == destination[1]:
                    if min(i, i2) <= destination[0] <= max(i, i2):
                        print(cnt)
                        return
                if (i2, j) not in explored:
                    new_to_explore.append((i2, j))
        to_explore = new_to_explore
        cnt += 1


main()
