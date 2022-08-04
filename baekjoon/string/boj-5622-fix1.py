# 다이얼

tel = input()
dial = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]
time = 0

for t in tel:
    for val in dial:
        if t in val:
            time += 3 + dial.index(val)

print(time)