# boj-3663과 동일 -> 추후 복습으로 다시 풀기
## 좌우조작은 인터넷 참고

def solution(name):
    answer = 0    # 최소 조작 횟수

    # 기준 아스키
    ascii_A = ord('A')
    ascii_Z = ord('Z')

    # 알파벳 조작은 A부터와 Z부터의 차이 중 작은 걸로 계산
    for n in name:
        num_move1 = ord(n) - ascii_A
        num_move2 = ascii_Z - ord(n) + 1    # A->Z로 움직이는거 +1
               
        if num_move1 < num_move2:
            answer += num_move1
        else:
            answer += num_move2

    # 좌우조작
    min_move = len(name) - 1    
    for i, _ in enumerate(name):
        next_i = i+1        

        # 연속되는 A 개수 구하기
        while next_i < len(name) and name[next_i] == 'A':
            next_i += 1
        
        # 각 문자부터 'A..'문자가 있을경우 몇번씩 조이스틱쓰는지 체크
        ## 1. 시작지점에서 오른쪽으로 쭉 가는 경우
        ## 2. 연속 A에서 오른쪽 먼저 탐색하고 왼쪽으로 돌아가는 경우
        ## 3. 왼쪽 먼저
        min_move = min(min_move, 2*i+ len(name)-next_i, 2*(len(name)-next_i)+i)

    return answer + min_move

#print(solution("AABC"))
print(solution("BBBBAAAABA"))
#print(solution("Z"))