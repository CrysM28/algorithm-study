# 2703. Cryptoquote




for _ in range(int(input())):
    crypt = input()
    key_list = list(input())

    keys = dict()
    idx = ord('A')

    for k in key_list:
        keys[chr(idx)] = k
        idx += 1
    
    ans = ""
    for c in crypt:
        if c not in keys:
            ans += c
        else:
            ans += keys[c]
    
    print(ans)