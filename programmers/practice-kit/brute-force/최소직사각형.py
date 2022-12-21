def solution(sizes):
    width, height = [], []

    for w, h in sizes:
        width.append(max(w, h))
        height.append(min(w, h))
    
    return max(width) * max(height)



print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))

'''


'''