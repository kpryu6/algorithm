'''
ICN 출발 여행경로
항공권 정보 tickets
ICN -> JFK
JND -> IAD

방문경로 return

3 <= 공항 수 <= 10000
항공권 모두 사용해야함
**가능경로 2개 이상일 경우, 알파벳 순서대로**
모든 도시 방문 가능

DFS
'''
from collections import defaultdict

def solution(tickets):
    
    G = defaultdict(list)
    not_sorted_G = defaultdict(list)
    
    # 그래프에 넣을 때부터 알파벳 역순으로 넣어버리기 - pop은 오른쪽부터 꺼내니까
    for s,d in sorted(tickets, reverse=True):
        G[s].append(d)
    
    answer = []
    stack = ["ICN"]
    
    # print(G)
    # {'SFO': ['ATL'], 'ICN': ['SFO', 'ATL'], 'ATL': ['SFO', 'ICN']})

    while stack:
        # cur = "ICN"
        cur = stack[-1]
        if not G[cur]:
            # 백트래킹
            answer.append(stack.pop())
        else:
            # 싹 연결
            next_d = G[cur].pop() # ATL
            stack.append(next_d)
        # print(G)
        # print(stack)
        
        
    return answer[::-1]
        
        
        
    
    