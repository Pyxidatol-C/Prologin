# https://prologin.org/train/2018/semifinal/recette
_ = input()
order = {n: i for i, n in enumerate(input().split())}
array = input().split()

cnt = 0


def merge(ls):
    global cnt
    n = len(ls)
    if n < 2:
        return ls
    mid = n // 2
    left = merge(ls[:mid])
    right = merge(ls[mid:])
    i, j = 0, 0
    new_ls = []
    while i < len(left) and j < len(right):
        if order[left[i]] < order[right[j]]:
            new_ls.append(left[i])
            i += 1
        else:
            new_ls.append(right[j])
            j += 1
            cnt += len(left) - i
    while i < len(left):
        new_ls.append(left[i])
        i += 1
    while j < len(right):
        new_ls.append(right[j])
        j += 1
        cnt += len(left) - i
    return new_ls


merge(array)
print(cnt % int(1e8 + 7))
