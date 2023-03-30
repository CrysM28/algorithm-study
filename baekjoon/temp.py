
words = []
for _ in range(5):
    words.append(list(input()))

ans = ''
for j in range(15):
    for i in range(5):
        try:
            ans += words[i][j]
        except:
            continue

print(ans)


#print(words)