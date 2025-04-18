def solution(genres, plays):
    answer = []
    d = {e : [] for e in set(genres)}
    
    for e in zip(genres, plays, range(len(plays))):
        d[e[0]].append([e[1], e[2]])
    
    # 장르 정렬
    sorted_genres = sorted(
        list(d.keys()), 
        key=lambda x: sum(map(lambda y: y[0], d[x])), reverse=True)
    
    # 장르에 따라 노래 정렬
    for g in sorted_genres:
        temp = [e[1] for e in sorted(d[g], key=lambda x: (-x[0], x[1]))]
        answer += temp[:min(len(temp), 2)]
    
    return answer
