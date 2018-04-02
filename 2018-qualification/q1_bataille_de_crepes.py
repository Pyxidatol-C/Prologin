# https://prologin.org/train/2018/qualification/bataille_de_crepe

n = int(input())
m1 = int(input())
m2 = int(input())
border = (m1 + m2) / 2
if border == n / 2:
    print(0)
elif border > n / 2:
    print(1)
else:
    print(2)
