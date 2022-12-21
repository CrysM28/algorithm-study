s, k, h = map(int, input().split())

if (s+k+h >= 100):
    print("OK")
else:
    m = min(s,k,h)
    if s == m:
        print("Soongsil")
    elif k == m:
        print("Korea")
    else:
        print("Hanyang")
