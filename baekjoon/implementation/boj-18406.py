# 18406. 럭키 스트레이트

def sum(x):
    result = 0
    for xx in x:
        result += int(xx)
    return result

n = input()
l = len(n)

left = n[:l//2]
right = n[l//2:]

if sum(left) == sum(right):
    print("LUCKY")
else:
    print("READY")