# 문자열 재정렬

new_str = input()
alph=[]
num=0

for s in new_str:
    if s.isalpha():
        alph.append(s)
    else:
        num += int(s)
    

alph.sort()

if num != 0:
    alph.append(str(num))

print(''.join(alph))