N = int(input())
cnt = 0

for i in range (N):
    word = list(input())
    a = list(set(word))     # 알파벳 전체 돌 필요 없이 있는 거로만 해도 되니까
    TF = 0                  # T/F 변수 -> 나는 그냥 boolean이 보기엔 편한듯 
    
    for i in range (len(word)-1):
        if(word[i]!=word[i+1]):     
            if word[i+1] in a:              # 처음 보는 단어는 a에 있고
                a.pop(a.index(word[i]))     # 한번 발견한 순간 a에서 없앰
            else:
                TF = 1      # a에 없으면 한 번 발견됐던 거니까 그룹단어가 아님
                break
    
    if TF == 0:
        cnt+=1
        
print(cnt)