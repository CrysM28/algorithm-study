word=[]

num=int(input())

for i in range(num):
    word=input()
    for j in range(1,len(word)):
        if word.find(word[j-1])>word.find(word[j]):
           num-=1
           break

print(num)
