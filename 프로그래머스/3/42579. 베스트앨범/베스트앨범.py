'''
많이 재생된 노래 2개씩 모아
재생 높은 순
1. 장르
2. 노래
3. 고유번호 낮은 노래 먼저 수록

베스트 앨범 노래 고유번호 순서대로 return
'''
def solution(genres, plays):
    answer = []
    from collections import defaultdict, Counter
    best = defaultdict(list)
    play_cnt = Counter()
    
    
    for i in range(len(genres)):
        play_cnt[genres[i]] += plays[i]
        best[genres[i]].append(i)
    
    # print(play_cnt)
    # print(best)
        
    # 장르 정렬
    sorted_genre = sorted(play_cnt, key=lambda x: -play_cnt[x])
    # print(sorted_genre)
    
    # 장르에 따른 노래 정렬
    for genre in sorted_genre:
        sorted_play = sorted(
            best[genre],
            key=lambda x: (-plays[x], x)
        )
        # print(sorted_play)
        answer.extend(sorted_play[:2])
    
    return answer