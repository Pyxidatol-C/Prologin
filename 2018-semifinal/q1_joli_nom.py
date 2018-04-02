# https://prologin.org/train/2018/semifinal/joli_nom

n = int(input())
for i in range(2 * n):
    if i % 2 == 0:
        input()  # Discard input.
    else:
        name = input()
        if not 5 <= len(name) <= 15:
            continue
        if not name[0].isalpha() or name[0].upper() != name[0]:
            continue
        for j in range(len(name) - 2):
            if name[j] == name[j + 1] == name[j + 2]:
                break
        else:
            print(name)
