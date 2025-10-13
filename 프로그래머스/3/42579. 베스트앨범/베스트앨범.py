'''
genre 별 베스트 2개씩 -> 베스트 엘범

1. 노래 많은 장르 먼저
2. 장르 안에서 재생높은거 먼저
3. 재생횟수 같으면 번호 낮은거 먼저

plays = 노래 별 재생 횟수

보기에는 고유번호는 index 인듯
return 베스트 앨범에 들어갈 노래 번호들 순서대로

defaultdict(<class 'list'>, {'classic': [(0,500), (2,150), (3,800)], 'pop': [600, 2500]})

장르 100개 미만이라는디;;
'''
from collections import defaultdict

def solution(genres, plays):
    answer = []
    music = defaultdict(list)
    for i,(x,y) in enumerate(zip(genres, plays)):
        music[x].append((i,y))
    
    # 어느 장르가 더 많이 재생됐는지 - 장르 정렬
    # 〉	['pop', 'classic']
    sorted_genre = sorted(
        list(music.keys()),
        key=lambda x: sum(map(lambda y: y[1], music[x])),
        reverse=True)

    # 그 장르에서 많이 재생된거는 뭔지
    # 재생 횟수 같은거 중 번호 낮은거 먼저
    for genre in sorted_genre:
        temp = [e[0] for e in sorted(music[genre],key=lambda x: (-x[1], x[0]))]
        answer += temp[:2]
    
    
    return answer



