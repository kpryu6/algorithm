# 완전 탐색
S = list(map(int, input().split()))
ans = 0
for a in S:
    x1 = a
    for b in S:
        # 수를 중복해서 사용하면 안 된다!
        if a == b:
            continue
        y1 = b
        for c in S:
            if a == c or b == c:
                continue
            x2 = c
            for d in S:
                if a == d or b == d or c == d:
                    continue
                y2 = d
                # 맨해튼 거리 계산
                dist = abs(x1 - x2) + abs(y1 - y2)
                # 가장 큰 값으로 정답 갱신
                ans = max(ans, dist)

print(ans)
