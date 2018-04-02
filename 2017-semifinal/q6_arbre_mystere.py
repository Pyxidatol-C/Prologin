# https://prologin.org/train/2017/semifinal/arbre_mystere
# Q6 shouldn't really be this easy ...

n = int(input())
backs = []
fronts = []
for _ in range(n):
    word = input()
    backs.append(word[:-1])
    fronts.append(word[1:])

fronts_copy, backs_copy = fronts.copy(), backs.copy()
for front in fronts:
    if front in backs_copy:
        fronts_copy.remove(front)
        backs_copy.remove(front)
if len(fronts_copy) == len(backs_copy) == 1:
    print("OUI")
else:
    print("NON")
