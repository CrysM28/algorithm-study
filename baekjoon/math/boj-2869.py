# 2869. 달팽이는 올라가고 싶다
import math

a, b, v = map(int, input().split())
day = math.ceil((v - a) / (a - b))      # a를 뺀 만큼만 올라가는 날 구하고
print(day + 1)                          # a 하나 올라가는만큼 +1
