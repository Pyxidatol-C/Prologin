# https://prologin.org/train/2015/semifinal/creneaux
n = int(input())
h = int(input())

castle = "\n".join(
    [" _  " * (n - 1) + " _",
     "_".join(["| |"] * n), ]
    + ["|" + " " * (4 * n - 3) + "|"] * (h - 2)
    + ["|" + "_" * (4 * n - 3) + "|"]
)
print(castle)
