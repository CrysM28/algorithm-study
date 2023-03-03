# 9020. 골드바흐의 추측

def is_prime(x):
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return False
    return True


for _ in range(int(input())):
    n = int(input())
    nums = [i for i in range(n)]
    left, right = n//2, n//2

    while left >=0 and right < n:
        val_l, val_r = nums[left], nums[right]
        val_sum = val_l + val_r

        if not is_prime(val_l):
            left -= 1
            continue 
        if not is_prime(val_r):
            right += 1
            continue     

        if val_sum == n:
            print(val_l, val_r)
            break
        elif val_sum > n:
            left -= 1
        else:
            right += 1
            
        
    
    
