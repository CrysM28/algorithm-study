# 다이얼

dial = {
    "ABC": 2,
    "DEF": 3,
    "GHI": 4,
    "JKL": 5,
    "MNO": 6,
    "PQRS": 7,
    "TUV": 8,
    "WXYZ": 9
}

tel = input()
time = 0

for t in tel:
    for val in dial.keys():
        for v in val:
            if t == v:
                time += 1 + dial[val]

print(time)