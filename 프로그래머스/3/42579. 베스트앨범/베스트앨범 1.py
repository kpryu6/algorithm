'''
장르 별로 많이 재생되 노래 2개씩

1. 재생 많이된 노래의 장르 수록
2. 재생 많이되 노래 수록
3. 고유 번호 낮은 거 먼저 수록 sort()

genres = 장르 배열
plays = 노래별 재생 횟수

베스트 앨범에 들어갈 노래 고유 번호 순서대로 출력

결론: plays의 고유번호를 정렬하는데, 많이 재생된 순서로 하되, 각 장르별 2개씩
'''

def solution(genres, plays):
    from collections import Counter, defaultdict
    answer = []
    
    play_cnt = Counter()
    best_plays = defaultdict(list)
        
    for i in range(len(genres)):
        genre = genres[i]
        play = plays[i]
        # {'pop': 3100, 'classic': 1450}
        play_cnt[genre] += play
        # {"classic" : [0, 2, 3], "pop" : [1, 4]}
        best_plays[genre].append(i)
    
    # 장르 정렬 (총 재생 수 기준)
    sorted_genres = sorted(play_cnt, key=lambda x: play_cnt[x], reverse=True)
    
    
    # best_plays[genres[i]]의 원소들 (고유번호들)을 plays에서 보고 그 값에 맞추어 정렬을 해야하는데..
    for genre in sorted_genres:
        # 해당 장르의 노래들 정렬
        sorted_songs = sorted(
            best_plays[genre], 
            # 재생 수 내림차순, 고유번호 오름차순
            key=lambda x: (-plays[x], x))
        
        answer.extend(sorted_songs[:2])
        
    return answer
