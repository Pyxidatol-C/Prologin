# https://prologin.org/train/2018/semifinal/composition_de_crepes
from itertools import combinations


def main():
    n, s = map(int, input().split())
    ls = sorted(map(int, input().split()))

    first = ls[:n // 2]
    second = ls[n // 2:]

    first_sums = set()
    for size in range((len(first) + 1)):
        for sub_ls in combinations(first, size):
            cur_sum = sum(sub_ls)
            if cur_sum == s:
                print("GAGNE")
                return
            first_sums.add(sum(sub_ls))

    for size in range(len(second) + 1):
        for sub_ls in combinations(second, size):
            if (s - sum(sub_ls)) in first_sums:
                print("GAGNE")
                return
    print("IMPOSSIBLE")


main()
