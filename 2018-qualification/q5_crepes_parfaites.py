# https://prologin.org/train/2018/qualification/crepes_parfaites

from math import log2, pi
from cmath import exp

L, n = map(int, input().split())
discs = [tuple(map(int, input().split())) for _ in range(n)]
p = []
cur = 0
for i in range(L):
    cur = discs[cur][bin(i).count('1') % 2]
    p.append(int(cur == 0))
p += [0] * L
if log2(2 * L) != int(log2(2 * L)):
    p += [0] * (2 ** (int(log2(2 * L)) + 1) - 2 * L)


def fft(X):
    N = len(X)
    if N == 1:
        return X
    even = fft(X[::2])
    odd = fft(X[1::2])
    T = [exp(-2j * pi * k / N) * odd[k] for k in range(N // 2)]
    return [even[k] + T[k] for k in range(N // 2)] + [even[k] - T[k] for k in range(N // 2)]


def ifft(X):
    N = len(X)
    if N == 1:
        return X
    even = ifft(X[::2])
    odd = ifft(X[1::2])
    T = [exp(2j * pi * k / N) * odd[k] for k in range(N // 2)]
    return [even[k] + T[k] for k in range(N // 2)] + [even[k] - T[k] for k in range(N // 2)]


def poly_squared(poly):
    return [round(abs(z / len(poly))) for z in ifft([x * x for x in fft(poly)])]


p_squared = poly_squared(p)
cnt = 0
for b, pos in enumerate(p[:L]):
    if pos == 1:
        cnt += p_squared[2 * b] // 2
print(cnt)
