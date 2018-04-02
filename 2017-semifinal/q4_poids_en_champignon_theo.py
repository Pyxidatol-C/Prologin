# https://prologin.org/train/2017/semifinal/poids_en_champignons
# TODO this passes all the correction tests, while it really should not.


def main():
    n, goal = map(int, input().split())
    weights = list(map(int, input().split()))
    weights.sort(reverse=True)
    candidates = []

    for weight in weights:
        for i in range(len(candidates)):  # for candidate in candidates does not work as ints are immutable
            if weight + candidates[i] == goal:
                print("OUI")
                return
            if weight + candidates[i] < goal:
                candidates[i] += weight
                break
        else:
            candidates.append(weight)
    print("NON")


main()
