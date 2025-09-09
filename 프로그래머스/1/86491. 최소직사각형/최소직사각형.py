'''
가로와 세로를 새로 정의
가로 = 주어진 가로,세로 중 긴 것
세로 = 주어진 가로,세로 중 짧은 것

최종 크기는 다 들어가야하니, 가로, 세로 중 가장 큰것들
'''
def solution(sizes):
    max_w = 0
    max_h = 0
    
    for w,h in sizes:
        longer = max(w,h)
        shorter = min(w,h)
        
        max_w = max(max_w, longer)
        max_h = max(max_h, shorter)
    
    answer = max_w * max_h
    return answer
