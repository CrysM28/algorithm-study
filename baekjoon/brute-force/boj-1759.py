# 1759. 암호 만들기

L, C = map(int, input().split())
words = input().split()
words.sort()

answer = []
visited = [0] * C
vowels = {'a', 'e', 'i', 'o', 'u'}


def make_pw(cnt, cur_i, pw, vowel, cons):
    if cnt == L:
        if vowel >= 1 and cons >= 2:
            answer.append(pw)
        return
    
    for i in range(C):
        if visited[i] == 0 and cur_i < i:
            new_vowel = vowel
            new_cons = cons
            if words[i] in vowels:
                new_vowel += 1
            else:
                new_cons += 1
            
            visited[i] = 1
            make_pw(cnt+1, i, pw + words[i], new_vowel, new_cons)
            visited[i] = 0


make_pw(0, -1, "", 0, 0)

print(*answer, sep='\n')


