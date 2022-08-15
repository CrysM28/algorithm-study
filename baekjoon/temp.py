# for easy problems

st = [int(input()) for _ in range(28)]
st.sort()

for i in range(1, 31):
    if i not in st:
        print(i)
