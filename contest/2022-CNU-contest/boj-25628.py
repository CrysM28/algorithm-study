# 25628. 햄버거 만들기

a, b = map(int, input().split())

hamburger = a // 2

if hamburger > b:
    hamburger = b

print(hamburger)