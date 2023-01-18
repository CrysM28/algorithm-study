def recursion(s, l, r):
    global rec
    if l >= r: return 1
    elif s[l] != s[r]: return 0
    else: 
        rec += 1
        return recursion(s, l+1, r-1)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1)


for _ in range(int(input())):
    rec = 1
    word = input()
    
    print(isPalindrome(word), rec)