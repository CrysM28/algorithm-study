def solution(answers):
    spj1, spj2, spj3 = spj1_fn(), spj2_fn(), spj3_fn()
    spj1_score, spj2_score, spj3_score = 0, 0, 0
    
    for a in answers:
        if a == next(spj1):
            spj1_score += 1
        if a == next(spj2):
            spj2_score += 1
        if a == next(spj3):
            spj3_score += 1
    
    total_score = {1: spj1_score, 2: spj2_score, 3: spj3_score}   
    answer = [k for k,v in total_score.items() if max(total_score.values()) == v] 
    return answer


# Generators for 수포자
def spj1_fn():
    while True:
        yield 1
        yield 2
        yield 3
        yield 4
        yield 5
        
def spj2_fn():
    while True:
        yield 2
        yield 1
        yield 2
        yield 3
        yield 2
        yield 4        
        yield 2
        yield 5
        
def spj3_fn():
    while True:
        yield 3
        yield 3
        yield 1
        yield 1
        yield 2
        yield 2
        yield 4
        yield 4
        yield 5
        yield 5