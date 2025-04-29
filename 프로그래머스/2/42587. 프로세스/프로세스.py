from collections import deque

def solution(priorities, location):
    queue = deque([(i, p) for i, p in enumerate(priorities)])
    order = 0

    while queue:
        cur = queue.popleft()

        # 우선순위가 더 높은 게 남아 있으면 다시 넣기
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        else:
            order += 1
            if cur[0] == location:
                return order
