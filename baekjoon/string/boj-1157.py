from collections import Counter

word=input().upper()
common_ord= Counter(word).most_common()

if len(common_ord) == 1:
    print(common_ord[0][0])
else:
    if common_ord[0][1] == common_ord[1][1]:
        print("?")
    else:
        print(common_ord[0][0])
