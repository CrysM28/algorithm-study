# 평균은 넘겠지

c = int(input())

for _ in range(c):
    all_input = list(map(int, input().split()))
    n, scores = all_input[0], all_input[1:]
    std_over_avg = [x for x in scores if x > sum(scores) / n]
    over_avg_rate = len(std_over_avg) / n * 100

    print("{:.3f}%".format(over_avg_rate))