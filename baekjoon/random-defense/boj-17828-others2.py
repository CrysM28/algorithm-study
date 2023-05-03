N, X = list(map(int, input().split(' ')))

ret = ''
if X > N * 26 or X < N:
    ret = '!'

else:
    s = ['A'] * N
    value = X - N

    for i in range(N):
        if value == 0:
            break

        s[N - 1 - i] = chr(min(value, 25) + ord('A'))

        value -= min(value, 25)

    ret = ''.join(s)

print(ret)