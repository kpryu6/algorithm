T = int(input())

for _ in range(T):
    N = int(input())
    table = list(map(int, input().split()))

    team_members = {}

    # 팀별 기록
    for i, team in enumerate(table):
        if team not in team_members:
            team_members[team] = []
        # 등수
        team_members[team].append(i+1) 

    # 6명 이상 팀만 필터링
    valid_teams = {team : ranks for team, ranks in team_members.items() if len(ranks) >= 6}
    
    # 유효한 팀별 개인 등수 정렬
    all_ranks = []
    for team, ranks in valid_teams.items():
        # pos 기준으로 sort를 하기 위해 pos를 앞으로
        all_ranks.extend((pos,team) for pos in ranks)
    all_ranks.sort()

    # 유효한 팀 대상 새로운 순위 및 점수
    score_list = {}
    for i, (pos,team) in enumerate(all_ranks):
        if team not in score_list:
            score_list[team] = []
        score_list[team].append(i+1)

    # 상위 4명 점수 및 우승팀
    min_score = float('inf')
    winner = -1
    for team, scores in score_list.items():
        team_score = sum(scores[:4])
        if team_score < min_score:
            min_score = team_score
            winner = team
        elif team_score == min_score:
            # 동점일 경우 5번째 비교
            if scores[4] < score_list[winner][4]:
                winner = team

    print(winner)
