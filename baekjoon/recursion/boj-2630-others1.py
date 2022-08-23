n, *paper = open(0)
n = int(n)
paper = [[*map(int, p.split())] for p in paper]


def count(paper, n):
    blue = any([1 in p for p in paper])
    white = any([0 in p for p in paper])
    if not blue: return 1, 0
    if not white: return 0, 1
    n2 = n // 2
    w1, b1 = count([p[:n2] for p in paper[:n2]], n2)
    w2, b2 = count([p[n2:] for p in paper[:n2]], n2)
    w3, b3 = count([p[:n2] for p in paper[n2:]], n2)
    w4, b4 = count([p[n2:] for p in paper[n2:]], n2)
    return w1 + w2 + w3 + w4, b1 + b2 + b3 + b4


w, b = count(paper, n)
print(w)
print(b)
