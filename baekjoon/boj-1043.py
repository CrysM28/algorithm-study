# 1043. 거짓말
import sys
input = sys.stdin.readline

people_num, party_num = map(int, input().split())
who_knows = list(map(int, input().split()))
lie = 0

know = [0 for _ in range(people_num+1)]
for w in who_knows:
    know[w] = 1


print(know)



# # 모든 파티에서 거짓말 가능
# if know[0] == 0:
#     party = [map(int, input().split()) for _ in range(M)]
#     lie = M

# # know가 없는 파티에서만 가능
# else:
#     for _ in range(M):
#         party = list(map(int, input().split()))
#         party = set(party[1:])

#         for i in range(know[0]):
#             if know[i+1] not in party:
#                 lie += 1


# print(lie)