
name = list(input())
name.sort()
print(name)

n = len(name)


def get_palindrome():
    idx = 0
    odd = ''
    pal = []

    while idx < n:
        #print(idx)
        first = name[idx]

        if idx >= n-1:
            second = ''
        else:
            second = name[idx+1]

        #print(first, second)

        if first == second:
            pal.append(first)
            idx += 1
        else:
            if odd:
                return ''
            else:
                odd = first
        
        idx += 1
    
    ans = ''.join(pal) + odd + ''.join(pal[::-1])

    #print(pal)
    
    return ans

half_pal = get_palindrome()

if not half_pal:
    print("I'm Sorry Hansoo")
else:
    print(half_pal)

#print(half_pal)