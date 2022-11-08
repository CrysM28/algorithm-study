def solution(genres, plays):
    answer = []
    
    dic = dict(dict())
    total_play = dict()

    for i in range(len(genres)):
        genre = genres[i]
        play = plays[i]
        
        if genre not in dic:
            dic[genre] = {i: play}
            total_play[genre] = play
        else:
            dic[genre][i] = play
            total_play[genre] += play


    total_play = sorted(total_play.items(), key = lambda x: x[1], reverse=True)
    
    for i in range(len(total_play)):
        genre = total_play[i][0]
        play = sorted(dic[genre].items(), key = lambda x: x[1], reverse=True)
                
        answer.append(play[0][0])
        if len(play) > 1:
            answer.append(play[1][0])

    return answer



'''
1. genre
2. plays
3. 고유번호

genre 별로 가장 많이 재생된 노래 2개 수록

그럼 dic 2개를 두고?

하나는 합을 세고
하나는 dict안에 dic 넣을까;
    dic 구성
    {genre: {play1: num1, play2: num2}}
    이런 식으로
    
    그래서 합먼저 정렬해서 2개 뽑고
    그 다음에 그 key를 가지고 2개 뽑는데
    play 순으로 정렬 하는 식으로?>


'''
