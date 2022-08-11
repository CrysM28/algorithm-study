import sys

input = sys.stdin.read


def sol1874():
    n, *nums = map(int, input().split())
    cur = 1
    st = []
    answer = []
    for num in nums:
        # 필요한 숫자가 나올때까지 push
        while cur <= num:
            st.append(cur)
            answer.append('+')
            cur += 1
        # 이제 위에 pop 했는데 필요한 숫자가 안 나온거면 안 되는거임
        if st[-1] != num:
            answer = ['NO']
            break
        # 그 외에는 정상적으로 pop
        st.pop()
        answer.append('-')
    print('\n'.join(answer))
   

if __name__ == '__main__':
    sol1874()